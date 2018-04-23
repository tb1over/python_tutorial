# chap 11 常见内建模块

content

# 1. datatime
datetime是Python处理日期和时间的标准库。
## 1.1 获取当前日期和时间
```python
from datetime import datetime
now = datetime.now()
print(now)
```
注意到```datetime```是模块，该模块还包含一个```datetime```类，通过```from datetime import datetime```导入的才是```datetime```这个类。

```datetime.now()```返回当前日期和时间，其类型是```datetime```。
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
```tuple```表示不变集合，例如，一个点的二维坐标就可以表示成：
```python
p = (1, 2)
```
但是很难看出这个```tuple```是用来表示一个坐标的.
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

```
正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：

username	password
michael	    e10adc3949ba59abbe56e057f20f883e
bob	    878ef96e86145580c38c87f0410ad153
alice	    99b1c2188db85afee403b1536010c2c9
```

# 6. hmac

# 7. itertools

# 8. contextlib

# 9. urllib

# 10. XML

# 11. HTMLParser