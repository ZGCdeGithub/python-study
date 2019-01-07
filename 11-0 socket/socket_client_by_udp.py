#!/usr/bin/env python
# coding=utf-8

import socket
import time


def client_fun():

    # 1.建立socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.发送消息到指定的服务器
    msg = 'hello, i am client'
    # 消息必须是bytes格式
    msg = msg.encode()
    # 发送消息
    sock.sendto(msg, ('127.0.0.1', 12138))

    # 3.接收返回信息
    data, addr = sock.recvfrom(500)
    # 解码返回内容
    data = data.decode()
    print('*******from {0} at {1}'.format(addr, time.strftime('%Y-%m-%d %H:%M:%S')))
    print(data)


if __name__ == '__main__':
    print('client start ……')
    client_fun()
    print('client end ……')
