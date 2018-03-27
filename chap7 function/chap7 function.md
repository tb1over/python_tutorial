#  第七章 函数
使用 ```def``` 语句定义函数是所有程序的基础。 本章的目标是讲解一些更加高级和不常见的函数定义与使用模式。 涉及到的内容包括默认参数、任意数量参数、强制关键字参数。 

### Content
<!-- TOC -->

- [第七章 函数](#第七章-函数)
        - [Content](#content)
    - [7.1 定义函数](#71-定义函数)
        - [7.1.1 向函数传递信息](#711-向函数传递信息)
        - [7.1.2 实参与形参](#712-实参与形参)
    - [7.2 传递参数](#72-传递参数)
        - [7.2.1 位置参数](#721-位置参数)
        - [7.2.2  默认值参数/可选参数](#722--默认值参数可选参数)
    - [7.3 返回值](#73-返回值)
        - [7.3.1 返回简单值](#731-返回简单值)
        - [7.3.2 返回字典](#732-返回字典)
    - [7.4 传递列表](#74-传递列表)
        - [7.4.1 在函数中修改列表](#741-在函数中修改列表)
        - [7.4.2 禁止修改参数列表](#742-禁止修改参数列表)
    - [7.5 传递任意数量的参数(可变参数)](#75-传递任意数量的参数可变参数)
    - [7.6 关键字参数](#76-关键字参数)
    - [7.7 命名(强制)关键字参数](#77-命名强制关键字参数)
    - [7.8 参数组合示例](#78-参数组合示例)
    - [7.9 作业](#79-作业)
    - [高级特性 -- 生成器](#高级特性----生成器)
    - [高级特性 -- 迭代器](#高级特性----迭代器)
    - [高级概念 -- 模块](#高级概念----模块)
        - [模块](#模块)
- [10](#10)
- [10](#10-1)

<!-- /TOC -->

## 7.1 定义函数
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回.
```python
def greet_user():
"""显示简单的问候语"""
    print("Hello!")

greet_user()
````
### 7.1.1 向函数传递信息
```python
def greet_user(username):
"""显示简单的问候语"""
    print("Hello, " + username.title() + "!")

greet_user('nxnu')
```
### 7.1.2 实参与形参
函数定义时参数列表中为形参，函数调用时参数列表中为实参。
## 7.2 传递参数
python中函数参数相对比较复杂，非常灵活。
### 7.2.1 位置参数
调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为**位置实参**
```python
def power(x):
    return x * x

power(3)    
```
其中x就是一个位置参数。
```python
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power(3,3)
```
其中x,n都是位置参数，并且函数调用时实参顺序不能错误。

### 7.2.2  默认值参数/可选参数
新的```power(x, n)```函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用.
```python 
power(5) 
```
这个时候，可以使用默认参数解决该问题。
```python
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
power(5)
power(5,3)
````
**注意：**
虽然默认参数带来了很大的便利性和灵活性，但是有需要注意的地方：
- 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。否则会出错。


## 7.3 返回值
### 7.3.1 返回简单值
```python
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

college = get_formatted_name('nxnu', 'sjxy')
print(college)
```
### 7.3.2 返回字典
函数可返回任何类型的值，包括列表和字典等较复杂的数据结构.
```python
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

college = build_person('nxnu', 'sjxy')
print(college)
```
```python
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

player = build_person('allen', 'iverson', age=27)
print(player)
```

## 7.4 传递列表
将列表传递给函数后，函数就能直接访问其内容。
```python
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
    print(msg)

usernames = ['allen', 'james', 'tony']
greet_users(usernames)
```
### 7.4.1 在函数中修改列表
将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这能够高效地处理大量的数据。
```python
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'huawei case', 'loongson case']
completed_models = []

print_models(unprinted_designs, completed_models)

show_completed_models(completed_models)
```

### 7.4.2 禁止修改参数列表
有时候，需要禁止函数修改列表(被调用的函数中，不能修改实参内容)。思考一下该怎么实现???
```python
......
print_models(unprinted_designs[:], completed_models)
......
```


## 7.5 传递任意数量的参数(可变参数)
顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个.
```python
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc([1, 2, 3]) # list
calc((1, 3, 5, 7)) # tuple
```
利用可变参数，可以让函数调用更简洁：
```python
# 这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 2) 
calc()
```
问题出现了：如果现在已经有了一个list或者tuple，需要调用calc函数，该怎么做???
```python
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])
```
其实不必，还有更好的方法：
```python
nums = [1, 2, 3]
calc(*nums)
```
## 7.6 关键字参数
有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。(本质上还是可变参数)

关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 可以只传入必选参数
person('Michael', 30) 

person('Bob', 35, city='Beijing')
# name: Bob age: 35 other: {'city': 'Beijing'}

person('Adam', 45, gender='M', job='Engineer')
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```
如果已经有了一个dict结构，该如何做，与上面可变参数类似的解决办法：
```python
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

person('Jack', 24, **extra)
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```
## 7.7 命名(强制)关键字参数
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过```kw```检查。
例如，希望检查 ```city```和```job```参数
```python
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
```

如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收```city```和```job```作为关键字参数，采用如下方法：
- 增加特殊分隔符
```python
# 需要一个特殊分隔符*,*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')
```
- 已有可变参数
```python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```
- 命名关键字具有缺省值(默认值)
```python
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')
```

## 7.8 参数组合示例
一个```*参数```只能出现在函数定义中最后一个位置参数后面，而 ```**参数```只能出现在最后一个参数。 有一点要注意的是，在```*参数```后面仍然可以定义命名(强制)关键字参数。
```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}

f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}

f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}

f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
```

```python
import html

def make_element(name, value, **attrs):
    #keyvals = [' %s="%s"' % item for item in attrs.items()]
    keyvals = [' %s="%s"' % (key,value) for key, value in attrs.items()]
    attr_str = ''.join(keyvals)

    elment = '<{name}{attrs}>{value}</{name}>'.format(
                name= name,
                attrs=attr_str,
                value=html.escape(value))
    return elment

# Example
# <div id="div1" clas="class1">test</div>
s = make_element('div', 'test', id='div1', clas='class1')
print(s)
```

```python
def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

minimum(1, 5, 2, -5, 10) # Returns -5
minimum(1, 5, 2, -5, 10, clip=0) # Returns 0
```
## 7.9 作业 
[慕课网-Python入门前7章](https://www.imooc.com/learn/177)

## 高级特性 -- 生成器
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

创建生成器的方法：
- 只要把一个列表生成式的[]改成()
```python
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>
```
怎么打印出g中的每个值呢?

next()函数获得generator的下一个返回值
```python
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> next(g)
16
>>> next(g)
25
>>> next(g)
36
>>> next(g)
49
>>> next(g)
64
>>> next(g)
81
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration           ## 可迭代对象
```
```python
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)
```
想想斐波那契数列。
```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
```
```python
fib(6)
1
1
2
3
5
8
'done'
```
fib函数其实定义了斐波那契数列的推算规则，这个规则的推算过程与生成器及其相似。
- yield
```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
```
```python
f = fib(6)
f
# <generator object fib at 0x104feaaa0>
```
generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值
```python
for n in fib(6):
    print(n)
```
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
```python
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
```

## 高级特性 -- 迭代器
可以直接作用于```for```循环的数据类型有以下几种:
- 一类是集合数据类型，如```list、tuple、dict、set、str```等；
- 一类是```generator```，包括生成器和带```yield```的```generator function```。

这些可以直接作用于for循环的对象统称为可迭代对象：```Iterable```。

可以使用```isinstance()```判断一个对象是否是```Iterable```对象：
```python
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False

```
可以被```next()```函数调用并不断返回下一个值的对象称为迭代器：```Iterator```。

可以使用```isinstance()```判断一个对象是否是```Iterator```对象：
```python
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False

```

综上，生成器都是```Iterator```对象，但```list、dict、str```虽然是```Iterable```，却不是```Iterator```。

可以使用```iter()```函数，将```Iterable```对象变为```Iterator```.

## 高级概念 -- 模块

### 模块
Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。

以内建的sys模块为例，编写一个hello的模块：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
```
导入```sys```模块后，就有了变量```sys```指向该模块，利用```sys```这个变量，就可以访问```sys```模块的所有功能。

```sys```模块有一个```argv```变量，用list存储了命令行的所有参数。```argv```至少有一个元素，因为第一个参数永远是该.py文件的名称

```python
if __name__=='__main__':
    test()
```
在命令行运行hello模块文件时，Python解释器把一个特殊变量```__name__```置为```__main__```，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试.

如果启动Python交互环境，再导入hello模块：
```python
Python 3.6.2 |Continuum Analytics, Inc.| (default, Jul 20 2017, 12:30:02) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import model_test
```
```python
model_test.test()
```

### 作用域
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过```_```前缀来实现的。
- 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
- 类似```__xxx__```这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的```__author__```，```__name__```就是特殊变量，model_test模块定义的文档注释也可以用特殊变量```__doc__```访问，我们自己的变量一般不要用这种变量名；
- 类似```_xxx```和```__xxx```这样的函数或变量就是非公开的（private），不应该被直接引用，比如```_abc```，```__abc```等；

```python
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
```
## 高级概念 -- 函数式编程
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
### 1. 高阶函数
- 变量可以指向函数
函数本身也可以赋值给变量，即：变量可以指向函数。
```python
>>> x = abs(-10)
>>> x
# 10
```
```python
>>> f = abs
>>> f
<built-in function abs>
```
```python
>>> f = abs
>>> f(-10)
# 10
```
- 函数名也是变量
```python
>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```
- 传入函数
一个函数就可以接收另一个函数作为参数，这种函数就称之为 **高阶函数** .
```python
def add(x, y, f):
    return f(x) + f(y)

add(-5, 6, abs)
```

### 2. map/reduce
### 3. filter
### 4. sorted

### 5. 返回函数

### 6. 匿名函数

### 7. 装饰器

### 8. 偏函数
