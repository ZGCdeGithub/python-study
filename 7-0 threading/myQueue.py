import threading
import time
import queue


class MsgQueue(threading.Thread):
    def __init__(self, que):
        super().__init__()
        self.que = que

    def run(self):
        while True:
            if self.que.qsize() > 0:
                print(self.que.get())


semphore = threading.Semaphore(3)


def fun(que=None):
    if semphore.acquire():
        prt = threading.currentThread().getName()+' is runing '
        # print(prt)
        que.put(prt)
        time.sleep(3)
        prt = threading.currentThread().getName()+' is end '
        que.put(prt)
        # print(prt)
        semphore.release()


if __name__ == '__main__':
    que = queue.Queue()
    q = MsgQueue(que)
    q.start()
    for i in range(8):
        t = threading.Thread(target=fun, args=(que,))
        t.start()
