#coding=utf8
import requests
import itchat
from itchat.content import *

KEY = '150ee9accc43492f95d7a7ae3de68fa0'
chatRooms=['wx_turing_test01', '本群']
def get_response(msg):
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register([TEXT], isGroupChat=True)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply =  ''# get_response(msg['Text'])

    if msg['MsgType'] == 1:        # 群消息
        # 消息来自于哪个群聊
        chatroom_id = msg['FromUserName']
 
        if 'NickName' in msg['User']:    
            chatroom_name = msg['User']['NickName']
        # 发送者的昵称
        username = msg['ActualNickName'] if msg['ActualNickName']!='' else '外星人'
        
        if msg['Type'] == TEXT:
            content = msg['Content']
        
        if 'wx_turing_test01' in chatRooms:             # if chatroom_name in charRooms:
            reply = '>>>来自 {chatroom_name}的{username} 发送：{content}'.format(
                chatroom_name=chatroom_name,
                username=username,
                content=content)
            
        # a or b的意思是，如果a有内容，那么返回a，否则返回b
        # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
            #return reply or defaultReply
            print(reply)
            # itchat.send_msg(reply, msg['ToUserName'])

    else:
        print(msg['Text'])
# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
itchat.run()
