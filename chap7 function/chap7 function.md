#  第七章 函数
使用 ```def``` 语句定义函数是所有程序的基础。 本章的目标是讲解一些更加高级和不常见的函数定义与使用模式。 涉及到的内容包括默认参数、任意数量参数、强制关键字参数、注解和闭包。 另外，一些高级的控制流和利用回调函数传递数据的技术在这里也会讲解到。

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