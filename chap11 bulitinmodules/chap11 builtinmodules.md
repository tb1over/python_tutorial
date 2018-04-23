# chap 11 常见内建模块

content

<!-- TOC -->

- [chap 11 常见内建模块](#chap-11-常见内建模块)
- [1. datatime](#1-datatime)
    - [1.1 获取当前日期和时间](#11-获取当前日期和时间)
    - [1.2 获取指定日期和时间](#12-获取指定日期和时间)
    - [1.3 datetime转换为timestamp](#13-datetime转换为timestamp)
    - [1.4 timestamp转换为datetime](#14-timestamp转换为datetime)
    - [1.5 str转换为datetime](#15-str转换为datetime)
    - [1.6 datetime转换为str](#16-datetime转换为str)
    - [1.7 datetime加减](#17-datetime加减)
    - [1.8 本地时间转换为UTC时间](#18-本地时间转换为utc时间)
    - [1.9 时区转换](#19-时区转换)
- [2. collections](#2-collections)
    - [2.1 namedtuple](#21-namedtuple)
    - [2.2 deque](#22-deque)
    - [2.3 defaultdict](#23-defaultdict)
    - [2.4 OrderedDict](#24-ordereddict)
    - [2.5 Counter](#25-counter)
- [3. base64](#3-base64)
    - [3.1Base的索引表](#31base的索引表)
    - [3.2 Base64原理](#32-base64原理)
    - [3.3 python内置的base64编码/解码](#33-python内置的base64编码解码)
- [4. struct](#4-struct)
- [5. hashlib](#5-hashlib)
    - [5.1 摘要算法简介](#51-摘要算法简介)
    - [5.2 md5](#52-md5)
    - [5.2 sha1](#52-sha1)
    - [5.3 摘要算法应用](#53-摘要算法应用)
    - [5.4 加盐](#54-加盐)
- [6. hmac](#6-hmac)
- [7. itertools](#7-itertools)
- [8. contextlib](#8-contextlib)
- [9. urllib](#9-urllib)
    - [9.1 GET](#91-get)
    - [9.2 Post](#92-post)
- [10. XML](#10-xml)
- [11. HTMLParser](#11-htmlparser)
- [12. 常见第三方模块](#12-常见第三方模块)

<!-- /TOC -->

# 1. datatime
datetime是Python处理日期和时间的标准库。
## 1.1 获取当前日期和时间
```python
from datetime import datetime
now = datetime.now()
print(now)
```
注意到```datetime```是模块，该模块还包含一个```datetime```类，通过```from datetime import datetime```导入的才是```datetime```这个类。

datetime.now()返回当前日期和时间，其类型是 datetime

## 1.2 获取指定日期和时间

要指定某个日期和时间，直接用参数构造一个datetime：
```python
from datetime import datetime
dt = datetime(2018, 4, 3, 16, 00) # 用指定日期时间创建datetime
print(dt)
```
## 1.3 datetime转换为timestamp
在计算机中，时间实际上是用数字表示的。把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
```python
# 可以理解
timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00

# 对应的北京时间
timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
```
**timestamp的值与时区毫无关系，全球各地的计算机在任意时刻的timestamp都是完全相同的。**
```python
from datetime import datetime
now = datetime.now()
print(now.timestamp()) # 1522742400.0
```
Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
## 1.4 timestamp转换为datetime
```python
from datetime import datetime
dt = datetime.now().timestamp() # timestamp

t = datetime.fromtimestamp(dt)
print(t)    # 2018-04-03 15:51:10.415029
```
注意：**timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换**

timestamp也可以直接被转换到UTC标准时区的时间
```python
from datetime import datetime
dt = datetime.now().timestamp() # timestamp

t = datetime.fromtimestamp(dt)
print(t)    # 2018-04-03 15:51:10.415029

t = datetime.utcfromtimestamp(dt)
print(t)    # 2018-04-03 07:51:10.415029
```
## 1.5 str转换为datetime
很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
```python
from datetime import datetime
cday = datetime.strptime('2018-4-3 16:05:00', '%Y-%m-%d %H:%M:%S')
print(cday)  # '2018-4-3 16:05:00', '%Y-%m-%d %H:%M:%S'
```
## 1.6 datetime转换为str
如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
```python
from datetime import datetime
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))  # Tue, Apr 03 16:06
```
关于日期格式字符请参考[python文档](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)

## 1.7 datetime加减
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入```timedelta```这个类：
```python
from datetime import datetime, timedelta
now = datetime.now()
now # datetime.datetime(2018, 4, 3, 16, 11, 45, 716812)

now + timedelta(hours=10)
# datetime.datetime(2018, 4, 4, 2, 11, 45, 716812)

now - timedelta(days=1)
# datetime.datetime(2018, 4, 2, 16, 11, 45, 716812)

now + timedelta(days=2, hours=12)
# datetime.datetime(2018, 4, 6, 4, 11, 45, 716812)
```
## 1.8 本地时间转换为UTC时间
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
```python
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
now
# datetime.datetime(2018, 4, 3, 16, 18, 19, 19613)

dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
dt
# datetime.datetime(2018, 4, 3, 16, 18, 19, 19613, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))
```
如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
## 1.9 时区转换
utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
```python
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt) # 2018-04-03 08:20:59.836526+00:00

# astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt) # 2018-04-03 16:20:59.836526+08:00

# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt) # 2018-04-03 17:20:59.836526+09:00

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2) # 2018-04-03 17:20:59.836526+09:00
```
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
- datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
- 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
# 2. collections
collections是Python内建的一个集合模块，提供了许多有用的集合类。
## 2.1 namedtuple
tuple表示不变集合，例如，一个点的二维坐标就可以表示成：
```python
p = (1, 2)
```
但是很难看出这个tuple是用来表示一个坐标的.
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)

p.x  # 1
p.y  # 2
```
用```namedtuple```函数可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

## 2.2 deque

使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
```python
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
```

## 2.3 defaultdict
## 2.4 OrderedDict
## 2.5 Counter
# 3. base64
为什么会有Base64编码呢？因为有些网络传送渠道并不支持所有的字节，比如图片二进制流的每个字节不可能全部是可见字符，所以就传送不了。最好的方法就是在不改变传统协议的情况下，做一种扩展方案来支持二进制文件的传送。把不可打印的字符也能用可打印字符来表示，问题就解决了。Base64编码应运而生，**Base64就是一种基于64个可打印字符来表示二进制数据的表示方法。**

## 3.1Base的索引表

(规定，不可更改)：

![Base的索引表](https://images0.cnblogs.com/blog/238451/201408/291137095326660.png)

## 3.2 Base64原理
如果是字符串转换为Base64码， 会先把对应的字符串转换为ascll码表对应的数字， 然后再把数字转换为2进制， 比如a的ascll码味97， 97的二进制是：01100001， 把8个二进制提取成6个，剩下的2个二进制和后面的二进制继续拼接， 最后再把6个二进制码转换为Base64对于的编码.
```c
字符串      a       b        c
ASCII      97      98       99
8bit   01100001 01100010 01100011
6bit   011000   010110   001001   100011
十进制      24      22        9        35
对应编码    Y        W        J        j
```

当转换到最后， 最后的字符不足3个字符咋办， 如果不足三个字符的话，我们直接在最后添加＝号即可， 具体可以参考以下两个字符串转换案例：

![](https://images0.cnblogs.com/blog/238451/201408/291217167983928.png)

## 3.3 python内置的base64编码/解码
```python
import base64

>>> base64.b64encode(b'http://www.nxnu.edu.cn')
b'aHR0cDovL3d3dy5ueG51LmVkdS5jbg=='

>>> base64.b64decode(b'aHR0cDovL3d3dy5ueG51LmVkdS5jbg==')
b'http://www.nxnu.edu.cn'
```
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
```python
>>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd++//

>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd--__'

base64.urlsafe_b64decode('abcd--__')
```
Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
# 4. struct
自学，作业
# 5. hashlib
## 5.1 摘要算法简介
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串。

摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
## 5.2 md5
```python
>>> import hashlib
>>> md5 = hashlib.md5()
>>> md5.update('nxnu.edu.cn'.encode('utf-8'))
>>> print(md5.hexdigest())
0b3b03ad609813b956731d67a4ef1488
```
MD5是最常见的摘要算法，速度很快，生成结果是固定的128bit字节，通常用一个32位的16进制字符串表示
## 5.2 sha1
与md5相类似
```python
>>> sha1=hashlib.sha1()
>>> sha1.update('nxnu.edu.cn'.encode('utf-8'))
>>> print(sha1.hexdigest())
30da1c36987e31d331c6b9b10ee6374e6d76193f
```
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

## 5.3 摘要算法应用
任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：
```
name	        password
michael	        123456
bob	        abc999
alice	        alice2008
```
明文存储--泄露、数据库管理员、运维人员


正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
```
username	password
michael	    e10adc3949ba59abbe56e057f20f883e
bob	    878ef96e86145580c38c87f0410ad153
alice	    99b1c2188db85afee403b1536010c2c9
```

```python
# -*- coding: utf-8 -*-
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

from hashlib import md5

def login(user,password):
    if db[user]==md5(password.encode()).hexdigest():
        return True
    else:
        return False

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
```
## 5.4 加盐
由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
```python
def calc_md5(password):
    return get_md5(password + 'the-Salt')
```
经过Salt处理的MD5口令，只要Salt不被别人知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
```python
import hashlib, random

db1 = {}

def register(username, password):
    db1[username] = User(username, password)

def get_md5(s):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username        # chr() 返回对应的字符
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(username + password + self.salt)

def login(username, password):
    user = db1[username]
    return user.password == get_md5(username + password + user.salt)

register('michael', '123456')
register('bob', 'abc999')
register('alice', 'alice2008')

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
```
# 6. hmac
如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。

这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。

和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
```python
# -*- coding: utf-8 -*-
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def register(username, password):
    db[username] = User(username, password)

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

register('michael', '123456')
register('bob', 'abc999')
register('alice', 'alice2008')

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
```
# 7. itertools
自学 作业
# 8. contextlib
自学 作业
# 9. urllib
urllib提供了一系列用于操作URL的功能。
## 9.1 GET
urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

例如，对豆瓣的一个URL https://api.douban.com/v2/book/1148282 进行抓取，并返回响应：
```python
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/1148282') as f:  # returns  http.client.HTTPResponse 
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
```
```json
Status: 200 OK
Date: Mon, 23 Apr 2018 14:45:32 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 3308
Connection: close
Vary: Accept-Encoding
X-Ratelimit-Remaining2: 94
X-Ratelimit-Limit2: 100
Expires: Sun, 1 Jan 2006 01:00:00 GMT
Pragma: no-cache
Cache-Control: must-revalidate, no-cache, private
Set-Cookie: bid=ohjjCCn3Xuo; Expires=Tue, 23-Apr-19 14:45:32 GMT; Domain=.douban.com; Path=/
X-DOUBAN-NEWBID: ohjjCCn3Xuo
X-DAE-Node: dis5
X-DAE-App: book
Server: dae
Data: {"rating":{"max":10,"numRaters":1889,"average":"9.5","min":0},"subtitle":"原书第2版","author":["Harold Abelson","Gerald Jay Sussman","Julie Sussman"],"pubdate":"2004-2","tags":[{"count":3177,"name":"计算机科学","title":"计算机科学"},{"count":2165,"name":"计算机","title":"计算机"},{"count":1917,"name":"编程","title":"编程"},{"count":1399,"name":"SICP","title":"SICP"},{"count":1134,"name":"程序设计","title":"程序设计"},{"count":893,"name":"经典","title":"经典"},{"count":662,"name":"LISP","title":"LISP"},{"count":626,"name":"Scheme","title":"Scheme"}],"origin_title":"Structure and Interpretation of Computer Programs","image":"https://img3.doubanio.com\/view\/subject\/m\/public\/s1113106.jpg","binding":"平装","translator":["裘宗燕"],"catalog":"出版者的话\n专家指导委员会\n序\n第2版前言\n第1版前言\n致谢\n第1章 构造过程抽象\n1.1 程序设计的基本元素\n1.2 过程与它们所产生的计算\n1.3 用高阶函数做抽象\n第2章 构造数据现象\n2.1 数据抽象导引\n2.2 层次性数据和闭包性质\n2.3 符号数据\n2.4 抽象数据的多重表示\n2.5 带有通用型操作的系统\n第3章 模块化、对象和状态\n3.1 赋值和
局部状态\n3.2 求值的环境模型\n3.3 用变动数据做模拟\n3.4 并发：时间是一个本质问题\n3.5 流\n第4章 元语言抽象\n4.1 元循环求值器\n4.2 Scheme的变形——惰性求值\n4.3 Scheme的变形——非确定性计算\n4.4 逻辑程序设计\n第5章
寄存器机器里的计算\n5.1 寄存器机器的设计\n5.2 一个寄存器机器模拟器\n5.3 存储分配和废料收集\n5.4 显式控制的求值器\n5.5 编译\n参考文献\n练习表\n索引","pages":"473","images":{"small":"https://img3.doubanio.com\/view\/subject\/s\/public\/s1113106.jpg","large":"https://img3.doubanio.com\/view\/subject\/l\/public\/s1113106.jpg","medium":"https://img3.doubanio.com\/view\/subject\/m\/public\/s1113106.jpg"},"alt":"https:\/\/book.douban.com\/subject\/1148282\/","id":"1148282","publisher":"机械工业出版社","isbn10":"7111135105","isbn13":"9787111135104","title":"计算机程序的构造和解释","url":"https:\/\/api.douban.com\/v2\/book\/1148282","alt_title":"Structure and Interpretation of Computer Programs","author_intro":"Harold Abelson是MIT1992年度MacVicarFacultyFellow。Gerald JaySussman是Matsushita电子工程教授。他们都在MIT电子工程和计算机科学系工作．都得到过最重要的计算机科学教育奖：如Abelson得到了IEEE计算机学会的Booth奖。Sussman得到了ACM的Karlstrom奖。\nJulie Sussman是作家和编辑，同时使用自然语言和计算机语言写作。","summary":"《计算机程序的构造和解释(原书第2版)》1984年出版，
成型于美国麻省理工学院(MIT)多年使用的一本教材，1996年修订为第2版。在过去的二十多年里，《计算机程序的构造和解释(原书第2版)》对于计算机科学的教育计划产生了深刻的影响。第2版中大部分重要程序设计系统都重新修改并做过测试
，包括各种解释器和编译器。作者根据其后十余年的教学实践，还对其他许多细节做了相应的修改。\n\n海报：","series":{"id":"1163","title":"计算机科学丛书"},"price":"45.00元"}
```

如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
```python
from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
```
## 9.2 Post
如果要以POST发送一个请求，只需要把参数data以bytes形式传入。后续有更详细的实验。

# 10. XML
自学，作业
# 11. HTMLParser
HTMLParser来非常方便地解析HTML，只需简单几行代码：
```python
# builtlib/htmlparser.py
```

# 12. 常见第三方模块
- Pillow
- requests
- chardet
- psutil
