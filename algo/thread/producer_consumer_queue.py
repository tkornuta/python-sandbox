# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Producer_Consumer_using_Queue.php

import threading
import time
import logging
import random
from queue import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

BUF_SIZE = 5
q = Queue(BUF_SIZE)

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                logging.debug(list(q.queue))
                item = random.randint(1,10)
                q.put(item)
                logging.debug('Putting ' + str(item)  
                                + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random()+1)
        return

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.name = name
        return

    def run(self):
        while True:
            #while q.empty():
            #    time.sleep(0.1)
            #    logging.debug("q empty :"+str(list(q.queue)))
            logging.debug(list(q.queue))
            item = q.get()
            logging.debug('Getting ' + str(item) 
                    + ' : ' + str(q.qsize()) + ' items in queue')
            time.sleep(random.random())
        return

if __name__ == '__main__':
    
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)