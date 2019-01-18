import requests

if __name__ == '__main__':
    url = 'http://wx.ngrok.znbest.com/test.php'
    proxy = {
        'http': '124.207.82.166:8008',
        'https': '220.180.50.14:53281'
    }
    rsp = requests.get(url, proxies=proxy)
    print(rsp.content.decode())
