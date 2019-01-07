#!/usr/bin/env python
# coding=utf-8

import socket
import time


def server_fun():

    # 1.建立socket，这个socket其实只负责接受对方的请求，真正通信的是链接后从新建立的socket
    # 使用ipv4和tcp协议
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定套接字（ip地址和端口号）
    sock.bind(('127.0.0.1', 12139))

    # 3.开始监听套接字
    sock.listen()

    # 死循环，让服务器一直运行下去
    while True:
        # 4.接受通信连接，
        # accept()返回一个tuple，包含通信socket和客户端地址
        skt, addr = sock.accept()

        while True:
            # 5.接受数据
            data = skt.recv(500)
            # 解码消息内容
            data = data.decode()
            print('connect from {0} at {1}'.format(addr, time.strftime('%Y-%m-%d %H:%M:%S')))
            print('     content: ', data)

            # 6.返回消息（非必须）
            if data == 'exit':
                reply = 'close'
            else:
                reply = 'reply at '+time.strftime('%Y-%m-%d %H:%M:%S')+': hello word'
            reply = reply.encode()
            skt.send(reply)

            if data == 'exit':
                break
        # 7.关闭连接
        skt.close()


if __name__ == '__main__':
    print('server start by tcp ……')
    server_fun()
    print('server end ……')
