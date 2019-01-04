#!/usr/bin/env python
# coding=utf-8

import threading
import multiprocessing
import queue
import time


class Customer(multiprocessing.Process):
    def __init__(self, que):
        super().__init__()
        self.que = que

    def run(self):
        while True:
            if self.que.qsize() > 0:
                item = self.que.get()
                print('customer cost product {0}'.format(item))


class Producter(multiprocessing.Process):
    def __init__(self, que):
        super().__init__()
        self.que = que

    def run(self):
        i = 0
        while True:
            self.que.put(i)
            print('producter product product {0}'.format(i))
            i += 1
            time.sleep(1)


def customer_fun(que):
    while True:
        if que.qsize() > 0:
            item = que.get()
            print('custom_fun cost {0}'.format(item))


def producter_fun(que):
    i = 0
    while True:
        que.put(i)
        print('product_fun product {0}'.format(i))
        time.sleep(1)
        i += 1


if __name__ == '__main__':
    # 多进程程序不能使用queue，必须使用multiprocessing.JoinableQueue
    que = queue.Queue()
    que = multiprocessing.JoinableQueue()
    # p1 = Customer(que)
    # p2 = Producter(que)
    # p1.start()
    # p2.start()
    p1 = multiprocessing.Process(target=producter_fun, args=(que,))
    c1 = multiprocessing.Process(target=customer_fun, args=(que,))
    p1.start()
    c1.start()
    p1.join()
    c1.join()
