import time
import threading

sumI = 0
loopSum = 1000000
# 生成一个锁
lock = threading.Lock()


def add_sum():
    global sumI, loopSum, lock
    for i in range(0, loopSum):
        # 加锁
        lock.acquire()
        sumI += 1
        # 释放锁
        lock.release()


def reduce_sum():
    global sumI, loopSum, lock
    for i in range(0, loopSum):
        # 加锁
        lock.acquire()
        sumI -= 1
        # 释放锁
        lock.release()


if __name__ == '__main__':
    print('起始值', sumI)
    # add_sum()
    # print('增加后', sumI)
    # reduce_sum()
    # print('减少后', sumI)

    # 使用多线程操作
    t1 = threading.Thread(target=add_sum, args=())
    t2 = threading.Thread(target=reduce_sum, args=())
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('结束后的值', sumI)
