import threading
import time


lock1 = threading.Lock()
lock2 = threading.Lock()


def fun1():
    # global lock1, lock2
    print('func1 starting ……')
    # 设置申请锁的有效期，超时则退出
    ret1 = lock1.acquire(timeout=4)
    if ret1:
        print('fun1 获得了 lock_1')
        time.sleep(2)
        print('fun1 正在申请 lock_2')
        ret2 = lock2.acquire(timeout=2)
        if ret2:
            print('func1 获得了 lock_2')
            lock2.release()
            print('fun1 释放了 lock_2')
        lock1.release()
        print('fun1 释放了 lock_1')
    print('fun1 end ……')


def fun2():
    print('fun2 starting ……')
    ret2 = lock2.acquire(timeout=4)
    if ret2:
        print('fun2 获得了 lock_2')
        time.sleep(4)
        print('fun2 正在申请 lock_1')
        ret1 = lock1.acquire(timeout=2)
        if ret1:
            print('fun2 获得了 lock_1')

            lock1.release()
            print('fun2 释放了 lock_1')
        lock2.release()
        print('fun2 释放了 lock_2')
    print('fun2 end ……')


if __name__ == '__main__':
    f1 = threading.Thread(target=fun1, args=())
    f2 = threading.Thread(target=fun2, args=())
    f1.start()
    f2.start()
