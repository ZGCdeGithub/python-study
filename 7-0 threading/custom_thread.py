import time
import threading


class MyThread(threading.Thread):
    """
    这是一个自定义线程类
    """
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def run(self):
        time.sleep(1)
        # print('')
        print('the thread index is {0}'.format(self.arg), end="\r\n")


for i in range(4):
    t = MyThread(i)
    t.start()

print('main end ')

