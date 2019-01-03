import time
import threading

sumI = 0
loopSum = 1000000


def add_sum():
    global sumI, loopSum
    for i in range(0, loopSum):
        sumI += 1


def reduce_sum():
    global sumI, loopSum
    for i in range(0, loopSum):
        sumI -= 1


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
