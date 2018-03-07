#coding=utf8
'''
https://www.zhihu.com/question/59524525
https://zhuanlan.zhihu.com/p/25782937

pip install numpy
pip install itchat
pip install Pillow
'''
from numpy import *
import itchat
import urllib
import requests
import os

import PIL.Image as Image
from os import listdir
import math

itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)[0:]

print(friends[0])

user = friends[0]["UserName"]


os.mkdir(user)

num = 0

for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(user + "/" + str(num) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1

pics = listdir(user)

numPic = len(pics)

#print(numPic)

eachsize = int(math.sqrt(float(640 * 640) / numPic))

#print(eachsize)

numline = int(640 / eachsize)

toImage = Image.new('RGB', (640, 640))


#print(numline)

x = 0
y = 0

for i in pics:
    path = user + '/' + i
    if os.path.getsize(path) == 0 :
        continue
    try:
        #打开图片
        img = Image.open(user + "/" + i)
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
        exit(1)
    else:
        #缩小图片
        img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
        #拼接图片
        toImage.paste(img, (x * eachsize, y * eachsize))
        x += 1
        if x == numline:
            x = 0
            y += 1

#print('done')
toImage.save(user + ".jpg")


itchat.send_image(user + ".jpg", 'filehelper')