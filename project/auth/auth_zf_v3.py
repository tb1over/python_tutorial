# -*-coding:utf-8-*-

import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar

import json
import base64

'''
模拟登录正方教务管理系统，使用python3.*
'''

url = 'http://172.16.2.135/'

# 用户名和密码
username = '82014014'
password = 'tb1over'


# 关于cookie 等open URLs时的扩展库说明
# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# cookie = cookielib.CookieJar()
cookie = http.cookiejar.CookieJar()

def get_security_image():
    
    # 将cookies绑定到一个opener cookie由cookielib自动管理
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

    # 用openr访问验证码地址,获取cookie
    picture = opener.open(url + 'CheckCode.aspx').read()

    # 保存图片
    with open('image.jpg', 'wb') as img:
        img.write(picture)

def get_security_code():
    security_code = get_code_auto()
    if(security_code == ''):
        security_code = input('Input Security code: ')
    
    return security_code

    # 可以利用在线识别?
    # https://www.juhe.cn/docs/api/id/60

def get_code_auto(m='GET'): 

    with open('image.jpg', 'rb') as f:
        base64_data = base64.b64encode(f.read())

    url = "http://op.juhe.cn/vercode/index"
    params = {
        "key" : "56b1b84a9a538a2a209114eb4d1e4c48", #申请到的APPKEY
        "codeType" : "8003", #验证码的类型，&lt;a href=&quot;http://www.juhe.cn/docs/api/id/60/aid/352&quot; target=&quot;_blank&quot;&gt;查询&lt;/a&gt;
        "base64Str" : base64_data, #图片文件
        "dtype" : "json", #返回的数据的格式，json或xml，默认为json
 
    }
    params = urllib.parse.urlencode(params)

    if m =="GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)
 
    content = f.read()
    res = json.loads(content)
    result = ''
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print('secret code:' + res["result"])
            result = res["result"]
        else:
            print("%s:%s" % (res["error_code"],res["reason"]))
    else:
        print("request api error")
    
    return result

def post_data():
    # 构造提交的表单
    # 注意页面用的是gb2312编码，python2中用unicode字符串，然后进行转码
    post_data = {
        '__VIEWSTATE': 'dDwxNTMxMDk5Mzc0Ozs+/hw9K6xUC9geRRrE7Q1dgj0f5dg=',
        'Button1': '',
        'hidPdrs': '',
        'hidsc': '',
        'lbLanguage': '',
        'RadioButtonList1': u'教师'.encode('gb2312'), 
        'Textbox1': '',
        'TextBox2': password,
        'txtSecretCode': get_security_code(),
        'txtUserName': username,
    }

    # 构造headers
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
    }

    # 生成post数据 ?key1=value1&key2=value2的形式
    # data = urllib.urlencode(post_data)
    data = urllib.parse.urlencode(post_data).encode('utf-8')

    # 构造request请求
    request = urllib.request.Request(url + 'default2.aspx', data, headers)
    # 构造opener,利用最初获取的cookie
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

    # response HTTP 302 Found 重定向,证明POST请求成功

    try:
        # gb2312的编码，需要解码
        response = opener.open(request)
        result = response.read().decode('gb2312')

        print('response : ' + str(response))

    except urllib.error.HTTPError as e:
        print('error code: ' + str(e.code))
        print('error info: ' + str(e))
        # print(e.info)
        print(e.geturl())           # redirect的地址,拿到这个地址就可以继续请求.注意携带cookie

def main():
    get_security_image()
    post_data()
    # get_code_auto()

if __name__ == '__main__': 
    main()