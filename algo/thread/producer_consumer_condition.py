# https://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/

import threading
import random
import time

class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, integers, condition):
        """
        Constructor.

        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition
        self.daemon = True
    
    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        while True:
            integer = random.randint(0, 256)
            if False:
                self.condition.acquire()
                print('{}: condition acquired'.format(self.name))
                self.integers.append(integer) 
                print('{}: {} appended to list'.format(self.name, integer))
                #print('{}: condition notification sent'.format(self.name))
                #self.condition.notify()
                print('{}: condition released'.format(self.name))
                self.condition.release()
            else:
                with self.condition:
                    print('{}: condition acquired'.format(self.name))
                    self.integers.append(integer) 
                    print('{}: {} appended to list'.format(self.name, integer))
                    print('{}: condition notification sent'.format(self.name))
                    self.condition.notify()
                print('{}: condition released'.format(self.name))
            # Sleep.
            time.sleep(0.45)

class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, integers, condition):
        """
        Constructor.

        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition
        self.daemon = True
    
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            self.condition.acquire()
            print('{}: condition acquired'.format(self.name))
            if self.integers:
                integer = self.integers.pop()
                print('{}: {} popped from list'.format(self.name, integer))
            print('{}: condition wait'.format(self.name))
            self.condition.wait()
            print('{}: condition released'.format(self.name))
            self.condition.release()


def main():
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers, condition)
    t3 = Consumer(integers, condition)

    # Start threads.
    t2.start()
    t3.start()
    t1.start()

    time.sleep(2)

    # End.
    #t1.join()
    #t2.join()
    #t3.join()

if __name__ == '__main__':
    main()
