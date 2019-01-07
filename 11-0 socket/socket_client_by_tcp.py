#!/usr/bin/env python
# coding=utf-8

import socket
import time


def client_fun():
    # 1.建立socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.与服务建立连接
    sock.connect(('127.0.0.1', 12139))

    while True:

        # 3.给服务器发送消息
        # msg = 'hello，i am client'
        msg = input('plesae input message：')
        sock.send(msg.encode())

        # 4.接收服务器反馈
        reply = sock.recv(500)
        reply = reply.decode()
        print(reply)
        if reply == 'close':
            break

    # 5.关闭socket连接
    sock.close()


if __name__ == '__main__':
    print('client start at {0}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
    client_fun()
    print('client end ……')

