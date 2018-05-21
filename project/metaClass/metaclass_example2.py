#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
__new__()方法接收到的参数依次是：

    1.当前准备创建的类的对象；

    2.类的名字；

    3.类继承的父类集合；

    4.类的方法集合。

"""


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type(name, bases, attrs)


"""
传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，
比如，加上新的方法，然后，返回修改后的定义。
"""


class MyList(list, metaclass=ListMetaclass):
    pass

l = MyList()
l.add(1)
print(l)


l2 = list()
l2.add(2)       # AttributeError: 'list' object has no attribute 'add'
print(l2)




