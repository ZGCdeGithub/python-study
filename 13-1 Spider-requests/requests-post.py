import requests

if __name__ == '__main__':
    baseurl = 'https://fanyi.baidu.com/sug?'
    # baseurl = 'http://wx.ngrok.znbest.com/test.php'
    # baseurl = 'http://wx.ngrok.znbest.com/mobile/index/check_quan.html'
    # 存放用来模拟form的数据一定是dict格式
    data = {
        # girl是翻译输入的英文内容，应该是由用户输入，此处使用硬编码
        'kw': 'girl'
    }
    # print(data)
    # 构造请求头
    headers = {
        'Content-Length': str(len(data)),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        # 'Cookie': 'BIDUPSID=26DE637105BD4F9D578C7669BE8BA82E; PSTM=1547531386; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=8E0A5EEFFE2313C87DC6972BB3D16509:FG=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; locale=zh; pgv_pvi=9121952768; delPer=0; PSINO=2; H_PS_PSSID=1469_21084_18560_28329_28131_26350_28266_27245_22073; ZD_ENTRY=baidu; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1547604664,1547697479; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1547697479'
    }
    rsp = requests.post(baseurl, data=data, headers=headers)
    print(rsp.text)
    print(rsp.json())
