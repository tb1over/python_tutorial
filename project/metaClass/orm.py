#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，
也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

编写底层模块的第一步，就是先把调用接口写出来。
比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，写出这样的代码：


class User(Model):
    #定义类的属性到列的映射
    pass

"""


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print('Found Model:%s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name

        return type.__new__(cls, name, bases, attrs)


# 基类Model
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r" 'Model' Object has no attribute '%s' " % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v.name)   # 字段的名称, v是一个Field的对象，Filed对象具有name, column_type属性
            params.append('?')
            args.append(getattr(self, k, None))     # 写入的值,从实例属性中查找到

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
print(User.__mappings__)
# 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# u = User()
# 保存到数据库：
# u.save()

