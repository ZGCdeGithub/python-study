import time
import threading


def now_time():
    """
    格式化时间
    :return:
    """
    return time.strftime('%Y-%m-%d %H:%M:%S')


def fun():
    print('subthread start at '+now_time())
    time.sleep(5)
    print('subthread end at '+now_time())


def main():
    print('main start at '+now_time())
    t1 = threading.Thread(target=fun, args=())
    t1.start()
    time.sleep(2)
    print('main end at '+now_time())


if __name__ == '__main__':
    main()
