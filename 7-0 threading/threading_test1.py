import time
import threading


def now_time():
    """
    格式化时间
    :return:
    """
    return time.strftime('%Y-%m-%d %H:%M:%S')


def loop1(name):
    print('loop1 start at '+now_time())
    print('loop1 ：', '我是'+name)
    time.sleep(2)
    print('loop1 end at '+now_time())


def loop2(name, sleep):
    print('loop2 start at '+now_time())
    print('loop2 : ', '我是'+name+'，我要睡'+str(sleep)+'秒')
    time.sleep(sleep)
    print('loop2 end at '+now_time())


def main():
    print('main start at '+now_time())
    # 创建两个子线程，并传递参数
    t1 = threading.Thread(target=loop1, args=('mick',))
    t2 = threading.Thread(target=loop2, args=('jone', 3))
    # 启动创建的子线程
    t1.start()
    t2.start()
    # 使用join(),让主线程等待子进程完成
    # t1.join()
    # t2.join()

    print('main end at '+now_time())


if __name__ == '__main__':
    main()
