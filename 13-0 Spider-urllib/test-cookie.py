from urllib import request, error, parse
import json

if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'
    try:
        data = {
            'kw': 'girl'
        }
        data = parse.urlencode(data).encode('utf-8')
        # 设置cookie
        headers = {
            'Content-Length': len(data),
            'Cookie': 'BIDUPSID=26DE637105BD4F9D578C7669BE8BA82E; PSTM=1547531386; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=8E0A5EEFFE2313C87DC6972BB3D16509:FG=1; H_PS_PSSID=1469_21084_18560_28131_26350_28266_27245_22073; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1547604664; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; delPer=0; PSINO=2; locale=zh; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1547624570'
        }

        req = request.Request(url, data=data, headers=headers)
        rsp = request.urlopen(req)
        cnt = rsp.read().decode()
        print(cnt)
        print(json.loads(cnt))
    except error.URLError as e:
        print(e)

