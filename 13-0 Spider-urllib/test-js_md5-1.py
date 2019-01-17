from urllib import request, parse, error


def translate(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15476902229857",
        "sign": "aa0802459e793bdf69a32ae5e8e71cb5",
        "ts": "1547690222985",
        "bv": "79162a91c7b783cde6a342e395e2b7ef",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    data = parse.urlencode(data).encode('utf-8')

    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        # "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=814485896@115.60.85.137; OUTFOX_SEARCH_USER_ID_NCOO=661894262.1764159; JSESSIONID=aaaDlhRhvNmtU8sgMHzHw; ___rl__test__cookies=1547690222982",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0( X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36 X-Requested-With: XMLHttpRequest"
    }

    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)
    cnt = rsp.read().decode()
    print(cnt)


if __name__ == '__main__':
    translate('teacher')
