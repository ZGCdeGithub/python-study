from urllib import request, error
import ssl
import chardet

# 将上下文环境改为非认证环境
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.12306.cn/mormhweb/'

try:
    rsp = request.urlopen(url)
    cnt = rsp.read()
    cs = chardet.detect(cnt)
    # print(cnt)
    with open('index.html', 'w', encoding='utf-8') as fp:
        fp.write(cnt.decode(cs.get('encoding', 'utf-8')))
except error.URLError as e:
    print(e)


