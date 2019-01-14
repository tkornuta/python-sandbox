# https://hackernoon.com/synchronization-primitives-in-python-564f89fee732

#barrier_tut.py

from random import randrange
from threading import Barrier, Thread, current_thread
from time import ctime, sleep

num = 4
# 4 threads will need to pass this barrier to get released.
b = Barrier(num)
names = ['Harsh', 'Lokesh', 'George', 'Iqbal']

def player():
    name = current_thread().name
    sleep(randrange(2, 5))
    print('%s reached the barrier at: %s' % (name, ctime()))
    b.wait()
    print('%s hugs the opponents' % (name))

    
threads = []
print('Race starts now...')

for i in range(num):
    threads.append(Thread(name=names[i],target=player))
    threads[-1].start()

"""
Following loop enables waiting for the threads to complete before moving on with the main script.
"""

for thread in threads:
    thread.join()
print('\nRace over!')