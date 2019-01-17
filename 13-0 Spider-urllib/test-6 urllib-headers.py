from urllib import request, error



if __name__ == '__main__':
    url = 'http://wx.ngrok.znbest.com/test.php'

    try:
        # //设置请求头
        # 1、直接用Request对象设置请求头
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        # }
        # req = request.Request(url=url, headers=headers)
        # 2、使用add_header方法添加请求头
        req = request.Request(url=url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19')

        rsp = request.urlopen(req)
        print(rsp)
        print(rsp.read().decode())
    except error.URLError as e:
        print(e.reason)

