# https://hackernoon.com/synchronization-primitives-in-python-564f89fee732

#rlock_tut.py

import threading

num = 0

if False:
    lock = threading.Lock()
    lock.acquire()
    num += 1
    lock.acquire() # This will block.
    num += 2
    lock.release()

if True:
    # With RLock, that problem doesn’t happen.
    lock = threading.RLock()

    lock.acquire()
    num += 3
    lock.acquire() # This won’t block.
    num += 4
    lock.release()
    lock.release() # You need to call release once for each call to acquire.