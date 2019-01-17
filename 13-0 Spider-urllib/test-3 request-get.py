from urllib import request, parse


if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    # wd = input("Input your keyword:")
    wd = 'python'
    qs = {'wd': wd}

    # 转换url编码
    query = parse.urlencode(qs)
    print(query)

    request_url = url + query
    print(request)

    r_url = url+'wd=python'
    print(r_url)

    rsp = request.urlopen(request_url)
    print(rsp.getcode())
    html = rsp.read()
    print(html)
