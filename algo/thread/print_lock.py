# https://www.youtube.com/watch?v=NwH0HvMI4EA

import threading
from queue import Queue
import time

print_lock = threading.Lock()

# Queue that will be shared accross threads.
q = Queue()

def thread_body():
    while True:
        # This is blocking - until an element won't appear in the queue.
        work_to_be_done = q.get()
        time.sleep(0.5)
        with print_lock:
            print("Thread {}: realized {}".format(threading.current_thread().name, work_to_be_done))
        # Inform queue that the task is done! (so join will proceed when all tasks will be finished!)
        q.task_done()

# Create threads working in the background - deamons.
for x in range(10):
    t = threading.Thread(target=thread_body)
    # Deamon will stop along with the main thread.
    t.daemon = True
    t.start()

start = time.time()

# Add "work" to be done.
for work_to_be_done in range(20):
    q.put(work_to_be_done)

# Wait until all tasks will be finished.
q.join()

print("Entire job took:", time.time() - start)
