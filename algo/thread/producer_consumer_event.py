# Classic producer consumer problem.
# Adding event to stop all threads at once (eliminates join) as presented in:
# https://stackoverflow.com/questions/18018033/how-to-stop-a-looping-thread-in-python

import threading
import time
import random

products = []
lock = threading.Lock()

pill2kill = threading.Event()

def producer(stop_event):
    global products
    t_name = threading.current_thread().name
    while not stop_event.is_set():
        # Produce.
        time.sleep(0.5)
        p = random.randint(1,10)
        print("{}: produced {}".format(t_name, p))
        with lock:
            print("{}: addded {} to list".format(t_name, p))
            products.append(p)

def consumer(stop_event):
    global products
    t_name = threading.current_thread().name
    while not stop_event.is_set():
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
        t = threading.Thread(target=producer, args={pill2kill})
        #t.daemon = True
        t.start()
        prods.append(t)

    # Start consumers.
    cons = []
    for i in range(5):
        t = threading.Thread(target=consumer, args={pill2kill})
        #t.daemon = True
        t.start()
        cons.append(t)

# Give them some time.
time.sleep(2)

# Finish them! ;)
print("Sending kill signal!")
pill2kill.set()
