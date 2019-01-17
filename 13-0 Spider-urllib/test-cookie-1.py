from urllib import request, parse, error
from http import cookiejar


# 创建cookiejar实例
my_cookie = cookiejar.CookieJar()
# 生成cookie管理器
my_cookie_handler = request.HTTPCookieProcessor(my_cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, my_cookie_handler)


def login(url):

    data = {
        'name': 'zgc',
        'pwd': '123456'
    }
    data = parse.urlencode(data).encode()

    req = request.Request(url, data=data)

    rsp = opener.open(req)
    cnt = rsp.read()
    print(cnt.decode())


def get_home(url):
    rsp = opener.open(url)
    cnt = rsp.read()
    print(cnt.decode())


if __name__ == '__main__':
    url = 'http://wx.ngrok.znbest.com/test.php'
    url2 = 'http://wx.ngrok.znbest.com/mine.php'
    get_home(url2)
    login(url)
    get_home(url2)
    print('*'*50)
    print(my_cookie)
    print('-'*50)
    for item in my_cookie:
        print('  ', '-' * 20)
        print(type(item))
        print(item)
        for i in dir(item):
            print('    ', i)


