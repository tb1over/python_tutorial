# -*- coding: utf8 -*-

"""
关于super函数以及MRO(Method Resolution Method)
"""


class Base(object):
    def __init__(self):
        print('enter Base')
        print('leave Base')


class A(Base):
    def __init__(self):
        print('enter A')
        super(A, self).__init__()
        print('leave A')


class B(Base):
    def __init__(self):
        print('enter B')
        super(B, self).__init__()
        print('leave B')


class C(A, B):
    def __init__(self):
        print('enter C')
        super(C, self).__init__()
        print('leave C')

c = C()

"""
1.
enter C
enter A
enter B
enter Base
leave Base
leave B
leave A
leave
2.
       Base
      /  \
     /    \
    A      B
     \    /
      \  /
       C

3.
MRO 列表:
对于你定义的每一个类，Python 会计算出一个方法解析顺序（Method Resolution Order, MRO）列表，
它代表了类继承的顺序，我们可以使用下面的方式获得某个类的 MRO 列表：
C.mro()   # or C.__mro__ or C().__class__.mro()
[__main__.C, __main__.A, __main__.B, __main__.Base, object]
该顺序按照C3线性化算法(广度优先)

4. super 原理

super 的工作原理如下：

def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]

其中，cls 代表类，inst 代表实例，上面的代码做了两件事：

    获取 inst 的 MRO 列表

    查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro[index + 1]

当你使用 super(cls, inst) 时，Python 会在 inst 的 MRO 列表上搜索 cls 的下一个类。

现在，让我们回到前面的例子。

首先看类 C 的 __init__ 方法：

super(C, self).__init__()

这里的 self 是当前 C 的实例，self.__class__.mro() 结果是：

[__main__.C, __main__.A, __main__.B, __main__.Base, object]

可以看到，C 的下一个类是 A，于是，跳到了 A 的 __init__，这时会打印出 enter A，并执行下面一行代码：

super(A, self).__init__()

注意，这里的 self 也是当前 C 的实例，MRO 列表跟上面是一样的，搜索 A 在 MRO 中的下一个类，发现是 B，
于是，跳到了 B 的 __init__，这时会打印出 enter B，而不是 enter Base。
"""