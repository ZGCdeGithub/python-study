#!/usr/bin/env python
# encoding=utf-8
from urllib import request
import chardet

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    rsp = request.urlopen(url)

    html = rsp.read()
    print(html)

    # 使用utf-8编码解码bytes
    # html = html.decode('utf-8')

    # 使用chardet检测编码
    cs = chardet.detect(html)
    print(cs)
    html = html.decode(cs.get('encoding', 'utf-8'))

    print(html)
