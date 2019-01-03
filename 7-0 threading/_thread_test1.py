import time
import _thread as thread


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
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thead
    # 参数两个，一个是需要运行的函数名，第二是函数的参数作为元祖使用，为空则使用空元祖
    # 注意：如果函数只有一个参数，需要参数后由一个逗号
    thread.start_new_thread(loop1, ('mick',))
    thread.start_new_thread(loop2, ('jone', 4))
    print('main end at '+now_time())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(6)



