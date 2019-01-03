import time
import threading


def now_time():
    """
    输出格式化后的当前时间
    :return:
    """
    return time.strftime('%Y-%m-%d %H:%M:%S')


def fun():
    print('daemon start at '+now_time())
    time.sleep(1)
    print('daemon end at '+now_time())


def loop():
    print('loop start at '+now_time())
    time.sleep(3)
    print('loop end at '+now_time())


def main():
    print('main start at '+now_time())
    t1 = threading.Thread(target=loop, args=())
    d1 = threading.Thread(target=fun, args=())
    d1.setDaemon(True)
    t1.setName('thr_1')
    d1.setName('dae_1')

    t1.start()
    d1.start()
    time.sleep(2)
    for thr in threading.enumerate():
        print('当前进程的名称是：{0}'.format(thr.getName()))
    print('还有{0}个进程在运行'.format(threading.activeCount()))
    print('main end at '+now_time())


if __name__ == '__main__':
    main()
