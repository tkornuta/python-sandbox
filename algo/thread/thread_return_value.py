# https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python

from threading import Thread

def foo(bar):
    print ('hello {0}'.format(bar))
    return "foo"

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        self._return = "foo from thread when it runs!"

    def join(self):
        Thread.join(self)
        return self._return

twrv = ThreadWithReturnValue(target=foo, args=('world!',))

twrv.start()
print (twrv.join())   # prints foo