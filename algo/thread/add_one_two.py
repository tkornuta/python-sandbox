# https://hackernoon.com/synchronization-primitives-in-python-564f89fee732
#lock_tut.py

from threading import Lock, Thread
import time
lock = Lock()
g = 0

def add_one():
    # Share variable
    global g
    lock.acquire()
    try:
        g += 1
    finally:
        lock.release()

def add_two():
    # Share variable.
    global g
    lock.acquire()
    try:
        g += 2
    finally:
        lock.release()

threads = []
# Create different threads with different functions.
for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()
    time.sleep(1)

# Wait for threads to end.
for thread in threads:
   thread.join()

print("g = ",g)