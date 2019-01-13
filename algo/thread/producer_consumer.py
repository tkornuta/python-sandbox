# Classic producer consumer problem.

import threading
import time
import random

products = []
lock = threading.Lock()

def producer():
    global products
    t_name = threading.current_thread().name
    while True:
        # Produce.
        time.sleep(0.5)
        p = random.randint(1,10)
        print("{}: produced {}".format(t_name, p))
        with lock:
            print("{}: addded {} to list".format(t_name, p))
            products.append(p)

def consumer():
    global products
    t_name = threading.current_thread().name
    while True:        
        with lock:
            if len(products) > 0:
                p = products.pop(0)
                print("{}: consuming {} from list".format(t_name, p))
        # Consume (or not).
        time.sleep(0.5)

if __name__ == "__main__":
    # Start producers.
    prods = []
    for i in range(5):
        t = threading.Thread(target=producer)
        #t.daemon = True
        t.start()
        prods.append(t)

    # Start consumers.
    cons = []
    for i in range(5):
        t = threading.Thread(target=consumer)
        #t.daemon = True
        t.start()
        cons.append(t)

# Give them some time.
time.sleep(3)

# Finish them! ;)
for prod in prods:
    prod.join()
for con in cons:
    con.join()
