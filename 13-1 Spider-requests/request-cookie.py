import requests


if __name__ == '__main__':
    url = 'http://wx.ngrok.znbest.com/test.php'
    rsp = requests.get(url)
    print(rsp.cookies)
    cookie_dict = requests.utils.dict_from_cookiejar(rsp.cookies)
    print(cookie_dict)
    print(cookie_dict['id'])
