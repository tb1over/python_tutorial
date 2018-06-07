# -*-coding:utf-8-*-

import urllib2
import cookielib
import urllib


'''
模拟登录正方教务管理系统，使用python2.*
'''

url = 'http://172.16.2.135/'

# 用户名和密码
username = '82014014'
password = 'tb1over'


# 关于cookie 等open URLs时的扩展库说明
# https://docs.python.org/2/library/urllib2.html?highlight=httpredirecthandler#urllib2.HTTPRedirectHandler.http_error_301
cookie = cookielib.CookieJar()

def get_security_image():
    
    # 将cookies绑定到一个opener cookie由cookielib自动管理
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    
    # 用openr访问验证码地址,获取cookie
    picture = opener.open(url + 'CheckCode.aspx').read()

    # 保存图片
    with open('image.jpg', 'wb') as img:
        img.write(picture)

def get_security_code():
    security_code = raw_input('Input Security code: ')
    return security_code

    # 可以利用在线识别?

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
    data = urllib.urlencode(post_data)

    # 构造request请求
    request = urllib2.Request(url + 'default2.aspx', data, headers)
    # 构造opener,利用最初获取的cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    # response HTTP 302 Found 重定向,证明POST请求成功
    # https://docs.python.org/2/howto/urllib2.html?highlight=httpredirecthandler
    try:
        # gb2312的编码，需要解码
        response = opener.open(request)
        result = response.read().decode('gb2312')

        print('response : ' + str(response))

    except urllib2.HTTPError as e:
        print('error code: ' + str(e.code))
        print('error info: ' + str(e))
        # print(e.info)
        print(e.geturl())           # redirect的地址,拿到这个地址就可以继续请求.注意携带cookie

def main():
    get_security_image()
    post_data()

if __name__ == '__main__': 
    main()