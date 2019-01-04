# !/usr/bin/env python
# coding=utf-8
import multiprocessing
import time


def producter(products, que):
    print('producter start ', time.ctime())
    for i in products:
        que.put(i)
        print('put {0} in que'.format(i))
    print('producter end ', time.ctime())


def customer(que):
    print('customer start ', time.ctime())
    while True:
        item = que.get()
        if item is None:
            break
        print('get {0} from que'.format(item))
        time.sleep(1)
        # que.task_done()
    print('customer end ', time.ctime())


if __name__ == '__main__':
    # 创建一个JoinableQueue
    que = multiprocessing.JoinableQueue()

    c = multiprocessing.Process(target=customer, args=(que,))
    c.daemon = True
    c.start()

    product = [1, 2, 3, 4]
    producter(product, que)
    que.put(None)
    # que.join()
    c.join()

