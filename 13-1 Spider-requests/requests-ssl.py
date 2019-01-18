import requests


if __name__ == '__main__':
    url = 'https://www.12306.cn'
    rsp = requests.get(url, verify=False)
    print(rsp.status_code)

