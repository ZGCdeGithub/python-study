"""
RLock 可重入锁
解决锁被多次申请，主要是递归中调用
可重入锁，申请了几次，就必须释放几次
"""
import threading
import time


mutex = threading.RLock()


class MyThread(threading.Thread):
    count = 0

    def run(self):
        if mutex.acquire():
            self.count += 1
            print(self.name+' run count '+str(self.count))
            mutex.acquire()
            mutex.release()
            mutex.release()


if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()
        time.sleep(1)
