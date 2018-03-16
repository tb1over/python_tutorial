#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from urllib import urlencode
from urllib2 import urlopen
import os,sys,re
import subprocess
import hashlib
import types

LOGIN = "http://10.10.10.6/"
LOGINOUT = "http://10.10.10.6/F.htm"

fid = "2"
constString = '12345678'

HelpMessage = '''\n********************************************************
                     Help Messge: 
 Please use your username and password for login dr.com!
             like this: python al.py sjxy01 123456 
*********************************************************              
'''

def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''

def post(url,data=None):
	if data:
		data = urlencode(data)
	print data
	response = urlopen(url, data)
	return response.read()

def login(username,userpass):  
	data={}
	data["DDDDD"] = username
	data["upass"] = userpass
	data["R1"] = 0
	data["R2"] = 1
	data["para"] = '00'
	data["0MKKey"] = 123456
	post(LOGIN,data)
	pass
def logout():
	post(LOGINOUT)

def netcheck(ip):
	try:
		p = subprocess.Popen(["ping -c 1 -w 1 "+ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
		out = p.stdout.read().decode()
		outerr = p.stderr.read().decode()
		regex = re.compile('100% packet loss')
		if len(regex.findall(out)) == 0:
			return 'OK'
		else:
			return 'NOT OK'  
	except:
		print 'check network error'
		return 'ERR'

def main(argv):

	if 0 == len(argv):
		print HelpMessage
		return
	username = argv[0]
	userpass = argv[1]
	print 'Your username:' + username 
	print 'Your password:' + userpass

	userpass = fid + userpass + constString
	userpass = md5(userpass) + constString + fid
        login(username, userpass)

#	if 'NOT OK' == netcheck('www.baidu.com'):
#		login(username,userpass)
#
#	if 'OK' == netcheck('www.baidu.com'):
#		print 'connect success, enjoy it !'
#	else:
#		print 'connect faile,please check the config of ip !'
#	while 'NOT OK' == netcheck('www.baidu.com'):
#		login(username,userpass)
#	while True:
#		if 'NOT OK' == netcheck('www.baidu.com'):
#			login(username,userpass)
#		if 'OK' == netcheck('www.baidu.com'):
#			print 'connect sucess,enjoy it!'
#		else:
#			print 'connect faile,please check the config of ip!'	

if __name__ == '__main__':  
	main(sys.argv[1:]);
