from urllib import request
from http import cookiejar

# 创建mozillaCookieJar实例
my_cookie = cookiejar.MozillaCookieJar()
my_cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
# 创建cookie管理器
my_cookie_handler = request.HTTPCookieProcessor(my_cookie)
# 创建http管理器
http_handler = request.HTTPHandler()
# 创建https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, my_cookie_handler)


def get_home(url):
    rsp = opener.open(url)
    cnt = rsp.read()
    print(cnt.decode())


if __name__ == '__main__':
    url2 = 'http://wx.ngrok.znbest.com/mine.php'
    get_home(url2)
