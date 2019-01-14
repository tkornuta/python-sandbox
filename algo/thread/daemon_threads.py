# https://www.bogotobogo.com/python/Multithread/python_multithreading_Daemon_join_method_threads.php

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def n():
    logging.debug('Starting')
    time.sleep(1)
    logging.debug('Exiting')

def d():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

if __name__ == '__main__':

    t = threading.Thread(name='non-daemon', target=n)

    d = threading.Thread(name='daemon', target=d)
    #d.setDaemon(True)
    d.daemon = True

    d.start()
    t.start()

    # Explicitly wait for daemon.
    #d.join()
    print ('({}) is alive? {}'.format(t.name, t.is_alive()))
    print ('({}) is alive? {}'.format(d.name, d.is_alive()))
    d.join(4.0)
    print ('({}) is alive? {}'.format(t.name, t.is_alive()))
    print ('({}) is alive? {}'.format(d.name, d.is_alive()))
    
