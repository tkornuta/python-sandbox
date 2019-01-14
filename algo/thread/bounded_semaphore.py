# https://stackoverflow.com/questions/48971121/what-is-the-difference-between-semaphore-and-boundedsemaphore

from threading import Semaphore, BoundedSemaphore

# Usually, you create a Semaphore that will allow a certain number of threads
# into a section of code.
s1 = Semaphore(5)

# When you want to enter the section of code, you acquire it first.
s1.acquire()

# Then you do whatever sensitive thing needed to be restricted to five threads.

# When you're finished, you release the semaphore.
s1.release()


# That's all fine, but you can also release it without acquiring it first.
s1.release()

# The counter is now 6! That might make sense in some situations, but not in most.

# If that doesn't make sense in your situation, use a BoundedSemaphore.

s2 = BoundedSemaphore(5)

s2.acquire()

s2.release()

try:
    s2.release()
except ValueError:
    print('As expected, it complained.')