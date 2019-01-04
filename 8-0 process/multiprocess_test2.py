# coding=utf-8
# !/usr/bin/env python3
import multiprocessing
import time


class MyProcess(multiprocessing.Process):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        print('这是一个派生Process类')
        time.sleep(self.interval)
        print('结束')


if __name__ == '__main__':
    p = MyProcess(3)
    p.start()
