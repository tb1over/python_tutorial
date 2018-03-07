#coding=utf8
import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

itchat.auto_login(hotReload=True)
itchat.run()
# 注意实验楼环境的中文输入切换
#itchat.send(u'测试消息发送', 'filehelper') 