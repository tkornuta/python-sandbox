# Author: tkornuta
# Date: 15/01/2019

import re
import time


import threading
from queue import Queue

# Queue that will be shared accross threads.
urls_to_investigate = Queue()

# Final list or urls.
url_lst = [] # Could also use set, as we need to store unique urls...
url_lst_lock = threading.Lock()

# Check terminal condition.
def parse_url(root_url, considered_url, get_hl_name):
    #print("considered_url",considered_url)
    # Get urls to investigate.
    sub_urls = get_hl_name(considered_url)
    #print("sub_urls=",sub_urls)
    for su in sub_urls:
        # Try to them one by one to query.
        try_to_add = False
        if su[0] == '/':
            # Add root url + sub_url
            if root_url[-1] == '/':
                root_su = root_url[:-1]
            else:
                root_su = root_url
            root_su += su[:]
            try_to_add = True
        elif (len(su) > len(root_url) and su[:len(root_url)] == root_url ):
            root_su = su
            try_to_add = True
        # Ok, check whether it is not in the dict already - critical section.
        with url_lst_lock:
            if try_to_add:
                if (root_su not in url_lst):
                    urls_to_investigate.put(root_su)
                    url_lst.append(root_su)
                    #print('url_lst',list(url_lst))

    # else: skip it.

def thread_body(root_url, get_hl_name):
    while True:
        # Block until an url won't appear in the queue.
        url = urls_to_investigate.get()
        # Parse it.
        parse_url(root_url, url, get_hl_name)
        # Inform that we are done.
        urls_to_investigate.task_done()

def crawl(root_url, n_workers, get_hl_name):
    
    # Add root.
    with url_lst_lock:
        url_lst.append(root_url)

    # Create threads working in the background - deamons.
    for _ in range(n_workers):
        t = threading.Thread(target=thread_body, args=(root_url, get_hl_name,))
        # Deamon will stop along with the main thread.
        t.daemon = True
        t.start()

    # Parse the root and add sub_urls to queue.
    parse_url(root_url, root_url, get_hl_name)
    
    # Wait until all tasks will be finished.
    urls_to_investigate.join()   
    return url_lst


#########################################################
# Test cases.

def get_hyperlinks_openai(url):
    web = {'https://www.openai.com': ['/jobs', 'https://blog.openai.com/learning-dexterity/', '/systems', '/about', '/press', '/research'], \
       'https://www.openai.com/jobs': ['/jobs', '/systems', '/about', '/press', '/research'], \
       'https://www.openai.com/press': ['/research', '/press', '/jobs', '/about', '/research', '/systems', 'https://arxiv.org/abs/1606.03498', 'https://universe.openai.com/', '/about'], \
       'https://www.openai.com/research': ['/requests-for-research', '/press', '/jobs', '/about', '/', '/research', '/systems'], \
       'https://www.openai.com/requests-for-research': ['https://tensorflow.org', 'http://www.maths.tcd.ie/~mnl/store/Amari1998a.pdf', 'https://gym.openai.com/envs/CartPole-v0', '/press', '/jobs', '/about', 'http://lstm.seas.harvard.edu/latex/', '/', '/research', '/systems'], \
       'https://www.openai.com/systems': ['/press', '/jobs', '/about', '/research', '/systems'], \
       'https://www.openai.com/about': ['/press', 'https://quip.com/', '/jobs', '/about', '/systems']}
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    assert re.match(regex, url) is not None, "%s is invalid url. Failing." % url
    time.sleep(0.02)
    return web.get(url, [])


def get_hyperlinks_binary(url):
    web = {'https://www.binary.com': ['https://www.binary.com/0', 'https://www.binary.com/1'], \
           'https://www.binary.com/1': ['https://www.binary.com/10', 'https://www.binary.com/11'], \
           'https://www.binary.com/10': ['https://www.binary.com/100', 'https://www.binary.com/101'], \
           'https://www.binary.com/11': ['https://www.binary.com/110', 'https://www.binary.com/111'], \
           'https://www.binary.com/100': ['https://www.binary.com/1000', 'https://www.binary.com/1001'], \
           'https://www.binary.com/101': ['https://www.binary.com/1010', 'https://www.binary.com/1011'], \
           'https://www.binary.com/110': ['https://www.binary.com/1100', 'https://www.binary.com/1101'], \
           'https://www.binary.com/111': ['https://www.binary.com/1110', 'https://www.binary.com/1111'], \
           'https://www.binary.com/1000': ['https://www.binary.com/10000', 'https://www.binary.com/10001'], \
           'https://www.binary.com/1001': ['https://www.binary.com/10010', 'https://www.binary.com/10011'], \
           'https://www.binary.com/1010': ['https://www.binary.com/10100', 'https://www.binary.com/10101'], \
           'https://www.binary.com/1011': ['https://www.binary.com/10110', 'https://www.binary.com/10111'], \
           'https://www.binary.com/1100': ['https://www.binary.com/11000', 'https://www.binary.com/11001'], \
           'https://www.binary.com/1101': ['https://www.binary.com/11010', 'https://www.binary.com/11011'], \
           'https://www.binary.com/1110': ['https://www.binary.com/11100', 'https://www.binary.com/11101'], \
           'https://www.binary.com/1111': ['https://www.binary.com/11110', 'https://www.binary.com/11111']}
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    assert re.match(regex, url) is not None, "%s is invalid url. Failing." % url
    time.sleep(0.02)
    return web.get(url, [])


def get_hyperlinks_wolfram(url):
    web = {'https://www.wolfram.com': ['https://community.wolfram.com', 'https://www.wolfram.com/contact-us', 'https://www.wolfram.com', 'https://www.wolfram.com/about', 'https://www.wolfram.com/education'], \
           'https://www.wolfram.com/education': ['/pro', '/web-apps', '/pro/pricing', '/pro/pricing'], \
           'https://www.wolfram.com/about': ['https://community.wolfram.com', 'https://www.wolfram.com/contact-us', 'https://www.wolfram.com', 'https://www.wolfram.com/about', 'https://www.wolfram.com/education'], \
           'https://www.wolfram.com/pro': ['/web-apps', '/pro/pricing', '/pro/pricing'], \
           'https://www.wolfram.com/examples/pro-features/image-input/index.html': ['/examples/mathematics/index.html', '/examples/society-and-culture/points-of-interest/index.html', '/examples/science-and-technology/materials/index.html', '/examples/science-and-technology/physics/index.html'], \
           'https://www.wolfram.com/examples/science-and-technology/engineering/index.html': ['/examples/mathematics/index.html', '/examples/society-and-culture/points-of-interest/index.html', '/input', '/examples/science-and-technology/materials/index.html']}
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    assert re.match(regex, url) is not None, "%s is invalid url. Failing." % url
    time.sleep(0.02)
    return web.get(url, [])

if __name__ == '__main__':

    # Test case 1:
    print(crawl('https://www.openai.com', 2, get_hyperlinks_openai))
    # TARGET: 
    # ['https://www.openai.com', 'https://www.openai.com/about', 
    # 'https://www.openai.com/jobs', 'https://www.openai.com/press', 
    # 'https://www.openai.com/requests-for-research', 
    # 'https://www.openai.com/research', 'https://www.openai.com/systems']

    # Test case 2:
    #print(crawl('https://www.binary.com', 3, get_hyperlinks_binary))

    # Test case 3:
    #print(crawl('https://www.wolfram.com', 2, get_hyperlinks_wolfram))
    # TARGET: 
    # ['https://www.wolfram.com', 'https://www.wolfram.com/about', 
    # 'https://www.wolfram.com/contact-us', 'https://www.wolfram.com/education', 
    # 'https://www.wolfram.com/pro', 'https://www.wolfram.com/pro/pricing', 
    # 'https://www.wolfram.com/web-apps']