from urllib import request


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp)

    # print('URL: {0}'.format(rsp.geturl()))
    print('*'*50)
    # print('Info: {0}'.format(rsp.info()))
    print('*' * 50)
    # print('Code：{0}'.format(rsp.getcode()))
    print(rsp.headers)
