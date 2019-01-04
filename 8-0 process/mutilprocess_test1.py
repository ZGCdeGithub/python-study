import multiprocessing
import time


def fun():
    print('fun start ……')
    time.sleep(5)
    print('end ……')


if __name__ == '__main__':
    print('__main__ start')
    # 创建进程
    p = multiprocessing.Process(target=fun())
    # 启动进程
    p.start()
    print('__main__ end')
