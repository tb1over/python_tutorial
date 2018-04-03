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

# 3. base64

# 4. struct

# 5. hashlib

# 6. hmac

# 7. itertools

# 8. contextlib

# 9. urllib

# 10. XML

# 11. HTMLParser