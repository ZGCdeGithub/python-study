'''
 程序顺序执行
'''
import time


def loop1():
    print('loop1 start at '+time.ctime())
    time.sleep(2)
    print('loop1 end at '+time.ctime())


def loop2():
    print('loop2 start at '+time.ctime())
    time.sleep(4)
    print('loop2 end at '+time.ctime())


def main():
    print('main start at '+time.ctime())
    loop1()
    loop2()
    print('main end at '+time.ctime())


if __name__ == '__main__':
    main()