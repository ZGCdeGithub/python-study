from urllib import request, error

if __name__ == '__main__':

    # URLError 当网络异常、连接失败、解析失败时
    # 是OSError的子类
    url = 'http://www.123edf.net'
    try:
        rsp = request.urlopen(url)
        print(rsp)
    except error.URLError as e:
        print(type(e))
        print(e)
        print(e.reason)

    # HTTPError,http协议错误，
    # HTTPError是URLError的子类
    url = 'http://www.sipo.gov.cn/www'
    try:
        rsp = request.urlopen(url)
        print(rsp)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print('连接失败')
