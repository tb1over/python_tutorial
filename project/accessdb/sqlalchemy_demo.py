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
user.name= 'zhangsan'
session.commit();
# 关闭session:


session.close()