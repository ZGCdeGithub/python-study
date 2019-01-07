#!/usr/bin/env python
# coding=utf-8

# 负责socket编程的模块
import socket
import time


def server_fun():

    # 1.建立socket连接，指定协议和通讯协议
    # socket.AF_INET 表示使用ipv4协议
    # socket.SOCKET.DGRAM 表示使用udp协议传输
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定ip和端口号
    # 绑定的套接字是一个tuple类型，地址和端口
    addr = ('127.0.0.1', 12138)
    sock.bind(addr)

    # 3.接收数据
    # 接收的是一个tuple类型，包括数据和客户端地址
    # 500表示一次接收500字节的数据
    data, addr = sock.recvfrom(500)

    print('***********一次数据接收-{0}************'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
    print(type(data), data)

    # 接收的数据是bytes格式，必须解码才能得到字符内容
    # decode()的默认参数就是utf-8
    text = data.decode()
    print(type(text), text)

    # 4.给客户端返回消息（非必须）
    reply = 'reply: '+text
    # 返回的内容必须是bytes格式
    reply = reply.encode()
    sock.sendto(reply, addr)


if __name__ == '__main__':
    print('server start ……')
    # server_fun()
    # 改进，让服务端一直运行，使用死循环方式
    while True:
        try:
            server_fun()
        except Exception as e:
            print('e')
        time.sleep(1)
    print('server end ……')

