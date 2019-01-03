import time
import threading
import queue


class Producter(threading.Thread):

    def __init__(self, que):
        super().__init__()
        self.queue = que

    def run(self):
        count = 0
        while True:
            if self.queue.qsize() <= 10:
                count += 1
                msg = '产品'+str(count)
                self.queue.put(msg)
                print(msg)
            time.sleep(1)


class Customer(threading.Thread):

    def __init__(self, que):
        super().__init__()
        self.queue = que

    def run(self):
        while True:
            if self.queue.qsize() > 10:
                msg = self.name+'消费了产品：'+str(self.queue.get())
                print(msg)
            time.sleep(1)


if __name__ == '__main__':
    # 生成一个队列
    que = queue.Queue()

    # 启动生产者
    p = Producter(que)
    p.start()

    # 启动消费者
    c = Customer(que)
    c.start()
