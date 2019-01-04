import threading
import time


def fun():
    print(' start ……')
    time.sleep(4)
    print(' end ……')


if __name__ == '__main__':
    t = threading.Timer(4, fun)
    t.start()

    i = 0
    while True:
        i += 1
        print(i, 'second')
        time.sleep(1)
