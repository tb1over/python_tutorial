#!/usr/bin/env python

import os
import re
import sys
import time
import types
import hashlib
import subprocess
from urllib import urlencode
from urllib2 import urlopen

LOGIN_ADDR = "http://10.10.10.6/"
LOGOUT_ADDR = "http://10.10.10.6/F.htm"
TARGET_HOST = "www.baidu.com"

fid = '1'
const_str = '12345678'

up_dict = {}
up_dict[0] = ("sjxy01", "2079035")
up_dict[1] = ("sjxy02", "123456")
up_dict[2] = ("sjxy03", "123456")
up_dict[3] = ("sjxy04", "123456")
up_dict[4] = ("sjxy05", "123456")
up_dict[5] = ("sjxy06", "123456")

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
        response = urlopen(url, data)
        return response.read()

def login(username, passwd):  
    data={}
    data["DDDDD"] = username
    data["upass"] = passwd
    data["R1"] = 0
    data["R2"] = 1
    data["para"] = 00
    data["0MKKey"] = 123456
    post(LOGIN_ADDR, data)
    pass

def logout():
    post(LOGOUT_ADDR)

def netcheck(ip_address):
    try:
        p = subprocess.Popen(["ping -c 1 -w 1 " + ip_address],
                             stdout = subprocess.PIPE, 
                             stderr = subprocess.PIPE,
                             shell = True)
        out = p.stdout.read().decode()
        outerr = p.stderr.read().decode()
        regex = re.compile('100% packet loss')
        if len(regex.findall(out)) == 0:
            return 'ACK'
        else:
            return 'NAK'  
    except:
        sys.stderr.write("check network error")
        return 'ERR'

def connect_auth_server():
    for idx in up_dict:
        username = up_dict[idx][0]
        passwd = up_dict[idx][1]
        passwd = fid + passwd + const_str
        passwd = md5(passwd) + const_str + fid

        if 'NAK' == netcheck(TARGET_HOST):
            login(username, passwd)

        result = netcheck(TARGET_HOST)
        if 'ACK' == result:
            sys.stdout.write("Connection success!")
            return True
        elif 'NAK' == result:
            continue
        else:
            sys.stderr.write("Connection fail!")
            return False

    return False

def patroller():
    while True:
        time.sleep(5)
        sys.stdout.flush()
        result = netcheck(TARGET_HOST)
        if 'ACK' == result:
            continue
        elif 'NAK' == result:
            if connect_auth_server():
                continue
            else:
                break
        else:
            break

def main():
    status = connect_auth_server()
    if status == True:
        patroller()
        sys.stdout.write("Connection is broken, please check the network!")
    else:
        sys.stderr.write("Please check the network configuration!")
    sys.stdout.flush()

def daemonize (stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):  
    try:   
        pid = os.fork()   
        if pid > 0:  
            sys.exit(0)
    except OSError, e:   
        sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror) )  
        sys.exit(1)  
  
    os.chdir("/")
    os.umask(0)
    os.setsid()
  
    try:   
        pid = os.fork()   
        if pid > 0:  
            sys.exit(0)
    except OSError, e:   
        sys.stderr.write("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror) )  
        sys.exit(1)  
  
    for f in sys.stdout, sys.stderr:
        f.flush()  
    si = open(stdin, 'r')  
    so = open(stdout, 'a+')  
    se = open(stderr, 'a+', 0)  
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())  
    os.dup2(se.fileno(), sys.stderr.fileno())  
  
if __name__ == '__main__': 
    daemonize('/dev/null', '/tmp/daemon_stdout.log', '/tmp/daemon_error.log')
    main()
