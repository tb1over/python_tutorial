#coding=utf8
'''

'''
import itchat
import csv


itchat.auto_login(hotReload=True)                   # 登陆微信

friends = itchat.get_friends(update=True)[1:]       # 获取好友信息list
headers = friends[0].keys()                         # 获取keys

    

with open('friends.csv', 'w', newline='',encoding='gb18030') as f:    ##写入文件,encoding why?
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader();
    f_csv.writerows(friends)

male = female = other =0
for friend in friends:
    if friend['Sex'] == 1:
        male += 1
    elif friend['Sex'] == 2:
        female += 1
    else:
        other += 1

#打印出自己的好友性别比例
total = len(friends)
print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
"女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
"不明性别好友： %.2f%%" % (float(other) / total * 100))

