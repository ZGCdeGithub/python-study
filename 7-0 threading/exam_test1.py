import time
import threading

loop = [4, 2]


class ThreadFun:
    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        """
        :param nloop: 函数名称
        :param nsec:  系统休眠时间
        :return:
        """
        print('start loop', nloop, time.ctime())
        time.sleep(nsec)
        print('end loop', nloop, time.ctime())


def main():
    print('main start at', time.ctime())
    t1 = threading.Thread(target=ThreadFun('loop1').loop, args=('loop1', 4))
    t = ThreadFun('loop2')
    t2 = threading.Thread(target=t.loop, args=('loop2', 2))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('main end at', time.ctime())


if __name__ == '__main__':
    main()

