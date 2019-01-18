from bs4 import BeautifulSoup
import requests
import re


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    rsp = requests.get(url)
    cnt = rsp.content
    soup = BeautifulSoup(cnt, 'lxml')
    content = soup.prettify()
    print(content)
    # tags = soup.find_all(re.compile('^me'), content='always')
    tags = soup.find_all(re.compile('^link'))
    for tag in tags:
        print(tag)

