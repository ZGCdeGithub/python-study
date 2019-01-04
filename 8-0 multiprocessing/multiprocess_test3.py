# !/usr/bin/env python
# coding=utf-8

import multiprocessing
import os
import time


def info_(title):
    print(title)
    print('__name__ = ', __name__)
    print('ppid：', os.getppid())
    print('pid：', os.getpid())


def pcs_fun():
    info_('process')
    print('process start ')
    time.sleep(3)
    print('process end')


if __name__ == '__main__':
    info_('__main__')
    p = multiprocessing.Process(target=pcs_fun)
    p.start()

