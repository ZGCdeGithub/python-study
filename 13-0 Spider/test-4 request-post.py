from urllib import request, parse
import json

if __name__ == '__main__':
    baseurl = 'https://fanyi.baidu.com/sug?'
    # baseurl = 'http://wx.ngrok.znbest.com/test.php'
    # baseurl = 'http://wx.ngrok.znbest.com/mobile/index/check_quan.html'
    # 存放用来模拟form的数据一定是dict格式
    data = {
        # girl是翻译输入的英文内容，应该是由用户输入，此处使用硬编码
        'kw': 'girl'
    }
    data = parse.urlencode(data).encode()
    # print(data)
    # 构造请求头
    headers = {
        'Content-Length': len(data),
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    # 打开请求
    baseurl = baseurl
    # 构造一个Request的实例
    req = request.Request(url=baseurl, data=data, headers=headers, method='GET')
    # 因为已经构造了一个Request的请求实例，则所有的请求信息都可以封装在Request实例中
    # rsp = request.urlopen(baseurl, data)
    rsp = request.urlopen(req)
    print(rsp)
    json_data = rsp.read().decode('utf-8')
    print(type(json_data))
    print('', json_data)

    # print(type(rsp.headers))
    print(rsp.geturl())


