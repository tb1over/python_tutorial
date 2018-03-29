import itchat
# import全部消息类型
from itchat.content import *


chatroomName=('wx_turing_test01', )
# 自动回复文本等类别的群聊消息
# isGroupChat=True表示为群聊消息
@itchat.msg_register([TEXT], isGroupChat=True)
def get_msg_text(msg):
    if msg['MsgType'] == 1:        # 群消息
        # 消息来自于哪个群聊
        chatroom_id = msg['FromUserName']
        chatroom_name = '本群'
        if 'NickName' in msg['User']:    
            chatroom_name = msg['User']['NickName']
        # 发送者的昵称
        username = msg['ActualNickName'] if msg['ActualNickName']!='' else '外星人'
        
        if msg['Type'] == TEXT:
            content = msg['Content']

        print('>>>来自 %s的  %s 发送 : %s' % (chatroom_name, username, content))
    else:
        pass
itchat.auto_login(hotReload=True)
itchat.run()
