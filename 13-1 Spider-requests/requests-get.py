import requests


if __name__ == '__main__':
    url = 'https://www.baidu.com/s?'

    # 使用get方法请求
    # rsp = requests.get(url)
    # print(rsp.status_code)

    # 使用request方法请求
    param = {
        'wd': 'python'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        # 'Cookie':'BIDUPSID=26DE637105BD4F9D578C7669BE8BA82E; PSTM=1547531386; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=8E0A5EEFFE2313C87DC6972BB3D16509:FG=1; locale=zh; pgv_pvi=9121952768; delPer=0; BD_HOME=0; BD_CK_SAM=1; PSINO=2; H_PS_PSSID=1469_21084_18560_28329_28131_26350_28266_27245_22073; ZD_ENTRY=baidu; H_PS_645EC=5e8aEEn2u57Pp94u%2FucSH%2BI6mt0tK4xn16vTXXbbhUqyEvinWQZ5snGoWJM; BDSVRTM=142'
    }
    # rsp = requests.request('get', url, params=param, headers=headers)
    rsp = requests.get(url, params=param, headers=headers)
    with open('index.html', 'w', encoding='utf-8') as fp:
        fp.write(rsp.content.decode())
    print(dir(rsp))
    print(rsp.content)
    print(rsp.url)
    print(rsp.request)
    print(rsp.headers)
    print(rsp.encoding)
    print(rsp.reason)
    print(rsp.raw)

