from urllib import request, error, parse
from http import cookiejar

# 指定存储cookie的文件
filename = 'cookies.txt'
# 实例化MozillaCookieJar
my_cookie = cookiejar.MozillaCookieJar(filename)
# 创建cookie管理器
my_cookie_handler = request.HTTPCookieProcessor(my_cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 创建https请求管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, my_cookie_handler)


def login(url):

    data = {
        'name': 'zgc',
        'pwd': '123456'
    }
    try:
        data = parse.urlencode(data).encode()

        req = request.Request(url, data=data)

        rsp = opener.open(req)
        # 将cookie保存到文件中
        # ignore_discard 表示即使cookie将要丢弃，也要保存
        # ignore_expires 表示即使cookie已经过期，也要保存
        my_cookie.save(ignore_discard=True, ignore_expires=True)
        cnt = rsp.read()
        print(cnt.decode())
    except error.URLError as e:
        print('登录失败', e)


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
    for item in my_cookie:
        print(item)
