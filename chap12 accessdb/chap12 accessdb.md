<!-- TOC -->

- [chap12 access database](#chap12-access-database)
- [1. 使用SQLite](#1-使用sqlite)
- [2. 使用MySQL](#2-使用mysql)
    - [2.1 安装、配置MySQL](#21-安装配置mysql)
    - [2.2 安装MySQL 驱动](#22-安装mysql-驱动)
    - [2.3 总结](#23-总结)
    - [3.4 ORM框架- SQLALchemy](#34-orm框架--sqlalchemy)

<!-- /TOC -->
# chap12 access database
程序运行的时候，数据都是在内存中的。当程序终止的时候，通常都需要将数据保存到磁盘上，无论是保存到本地磁盘，还是通过网络保存到服务器上，最终都会将数据写入磁盘文件。
存储方式：
- 文件csv, json, binary
- 数据库
讨论，有点有哪些???

常见数据库分类：
- 关系型数据库
Oracle, SQL Server, DB2, Sybase；MySQL(MariaDB), PostgreSQL, sqlit; 达梦,GBase南大通用,金仓,SequoiaDB巨杉数据库
- NoSQL

Not Only Sql，存储方式、存储结构、存储规范、存储扩展、查询方式、事务、性能.....等方面与关系型数据库完全不同。
Redis, Memcache, MongoDb

# 1. 使用SQLite
SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。

Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。

需要明确的概念：
- 表
- 数据库连接: Connection
- 游标: Cursor

Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
```python
# 导入SQLite驱动:
>>> import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
>>> conn = sqlite3.connect('test.db')
# 创建一个Cursor:
>>> cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
<sqlite3.Cursor object at 0x10f8aa260>
# 继续执行一条SQL语句，插入一条记录:
>>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
<sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数:
>>> cursor.rowcount
1
# 关闭Cursor:
>>> cursor.close()
# 提交事务:
>>> conn.commit()
# 关闭Connection:
>>> conn.close()
```
查询记录
```python
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
# 执行查询语句:
>>> cursor.execute('select * from user where id=?', ('1',))
<sqlite3.Cursor object at 0x10f8aa340>
# 获得查询结果集:
>>> values = cursor.fetchall()
>>> values
[('1', 'Michael')]
>>> cursor.close()
>>> conn.close()
```
使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。


如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
```python
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
```

```python
# 案例：根据分数段查找指定的名字
# sqlite_demo.py
'''
select * from user where score between 70 and 95 order by score;
select * from user where score>=70 and score<=95 order by score;
'''
```

# 2. 使用MySQL
MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。

## 2.1 安装、配置MySQL
自学
在Windows上，安装时请选择UTF-8编码，以便正确地处理中文
```sql
show variables like '%char%';
```
```sql
/*my.ini*/
[client]
default-character-set=utf8

[mysqld]
character_set_server=utf8
init_connect='SET NAMES utf8'
```
## 2.2 安装MySQL 驱动

```python
pip install mysql-connector-python --allow-external mysql-connector-python
```

```python
# 导入MySQL驱动:
>>> import mysql.connector
# 注意把password设为你的root口令:
>>> conn = mysql.connector.connect(user='root', password='password', database='test')
>>> cursor = conn.cursor()
# 创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
>>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
>>> cursor.rowcount
1
# 提交事务:
>>> conn.commit()
>>> cursor.close()
# 运行查询:
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id = %s', ('1',))
>>> values = cursor.fetchall()
>>> values
[('1', 'Michael')]
# 关闭Cursor和Connection:
>>> cursor.close()
True
>>> conn.close()
```
## 2.3 总结
- 执行INSERT等操作后要调用commit()提交事务；
- MySQL的SQL占位符是%s。

## 3.4 ORM框架- SQLALchemy
数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，可以用一个list表示多行，list的每一个元素是tuple，表示一行记录，比如，包含id和name的user表：
```python
[
    ('1', 'Michael'),
    ('2', 'Bob'),
    ('3', 'Adam')
]
```
但是用tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来：
```python
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')   
]
```
这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。
在Python中，最有名的ORM框架是SQLAlchemy。

首先通过pip安装SQLAlchemy：
```python
 pip install sqlalchemy
```
```python
# accessdb/sqlalchemy.py

# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:  
# echo=True打印操作信息
engine = create_engine('mysql+mysqlconnector://root:bobo1over@localhost:3306/test', echo=True)

# 创建DBSession类型: 
DBSession = sessionmaker(bind=engine)


# 创建session对象: (connect)
session = DBSession()

'''
# 1. 查询数据
user=session.query(User).filter(User.id=='1').one()
print(user.name)
'''

'''
# 2.添加数据
# 创建新User对象:
new_user = User(id='2', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
'''

'''
# 3. 删除数据
u=session.query(User).filter(User.id=='2').one()
session.delete(u)
session.commit()
'''

# 4. update
user=session.query(User).filter(User.id=='5').one()
user.name= 'Allen'
session.commit();
# 关闭session:
session.close()
```

如果有一对多的表连接关系：
```python
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
```