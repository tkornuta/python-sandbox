#semaphores_tut.py

import random, time
from threading import BoundedSemaphore, Thread

max_items = 5

"""
Consider 'container' as a container, of course, with a capacity of 5
items. Defaults to 1 item if 'max_items' is passed.
"""
container = BoundedSemaphore(max_items)

def producer(nloops):
    #for i in range(nloops):
    while(1):
        time.sleep(random.randrange(1, 2))
        print(time.ctime(), end=": ")
        if container.acquire(False):
            print("Produced an item.")
        else:
            print("Full, skipping.")

def consumer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(4, 5))
        print(time.ctime(), end=": ")

        """
        In the following if statement we disable the default
        blocking behaviour by passing False for the blocking flag.
        """

        try:
            container.release()
            print("Consumed an item.")
        except ValueError:
            print("Empty, skipping.")

threads = []
nloops = random.randrange(3, 6)
print("Starting with %s items." % 0)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(random.randrange(nloops, nloops+max_items+2),)))

for thread in threads:  # Starts all the threads.
    thread.start()
for thread in threads:  # Waits for threads to complete before moving on with the main script.
    thread.join()
print("All done.")