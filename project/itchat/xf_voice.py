#-*- coding: utf-8 -*-
import requests
import re
import time
import hashlib
import base64
import struct
import json

URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "raw"
APPID = "5abbaec3"
API_KEY = "31d204d68b818367672e924b9bcd20a8"

def getHeader():
        # 构造输出音频配置参数
        Param = {
            "auf": "audio/L16;rate=16000",    #音频采样率
            "aue": "lame",    #音频编码，raw(生成wav)或lame(生成mp3)
            "voice_name": "xiaoyan",
            "speed": "50",    #语速[0,100]
            "volume": "77",    #音量[0,100]
            "pitch": "50",    #音高[0,100]
            "engine_type": "aisound"    #引擎类型。aisound（普通效果），intp65（中文），intp65_en（英文）
        }
        # 配置参数编码为base64字符串，过程：字典→明文字符串→utf8编码→base64(bytes)→base64字符串
        Param_str = json.dumps(Param)    #得到明文字符串
        Param_utf8 = Param_str.encode('utf8')    #得到utf8编码(bytes类型)
        Param_b64 = base64.b64encode(Param_utf8)    #得到base64编码(bytes类型)
        Param_b64str = Param_b64.decode('utf8')    #得到base64字符串
        
        time_now = str(int(time.time()))
        checksum = (API_KEY + time_now + Param_b64str).encode('utf8')
        checksum_md5 = hashlib.md5(checksum).hexdigest()
        header ={
                'X-CurTime':time_now,
                'X-Param':Param_b64str,
                'X-Appid':APPID,
                'X-CheckSum':checksum_md5,
                'X-Real-Ip':'127.0.0.1',
                'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
        }
        return header

def getBody(text):
        data = {'text':text}
        return data

def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()

r = requests.post(URL,headers=getHeader(),data=getBody("科大讯飞是中国最大的智能语音技术提供商 宁夏师范学院数学与计算机科学学院"))
contentType = r.headers['Content-Type']
if contentType == "audio/mpeg":
    sid = r.headers['sid']
    if AUE == "raw":
        writeFile("audio/"+sid+".wav", r.content)
    else :
        writeFile("audio/"+sid+".mp3", r.content)
    print("success, sid = " + sid)
else :
    print(r.text) 