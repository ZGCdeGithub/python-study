# coding=utf-8
from urllib import request, error
import json


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    url = 'http://wx.ngrok.znbest.com/test.php'

    # 设置代理
    # 1、设置代理地址
    proxy = {'http': '124.207.82.166:8008'}
    # 2、创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3、创建opener
    opener = request.build_opener(proxy_handler)
    # 4、安装opener
    request.install_opener(opener)
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        print(rsp)
        html = rsp.read().decode()
        json_data = json.loads(html)
        print(type(json_data))
        for k, v in json_data.items():
            print(k, ':', v)
    except error.URLError as e:
        print(e)

