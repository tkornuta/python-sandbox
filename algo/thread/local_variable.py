# https://www.bogotobogo.com/python/Multithread/python_multithreading_Thread_Local_Specific_Data.php

import threading
import logging
import random
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-0s) %(message)s',)

def show(d):
    try:
        val = d.val
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)

def f(d):
    show(d)
    d.val = random.randint(1, 100)
    show(d)

class MyLocal(threading.local):
    def __init__(self, v):
        logging.debug('Initializing %r with %d', self, v)
        self.val = v

if __name__ == '__main__':
    if False:
        d = threading.local()
        show(d)
        d.val = 999
    else:
        d = MyLocal(997)
        d.val = 151
    show(d)

    for i in range(2):
        d.val = i
        show(d)
        t = threading.Thread(target=f, args=(d,))
        t.start()

