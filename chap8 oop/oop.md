# 第八章 面向对象编程
面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

## Content

<!-- TOC -->

- [第八章 面向对象编程](#第八章-面向对象编程)
    - [Content](#content)
    - [8.1 简介](#81-简介)
    - [8.2 类和实例](#82-类和实例)
        - [8.2.1 类的定义和实例化](#821-类的定义和实例化)
        - [8.2.2 构造函数](#822-构造函数)
        - [8.2.3 数据封装](#823-数据封装)
    - [8.3 访问控制](#83-访问控制)
    - [8.4 继承和多态](#84-继承和多态)
        - [8.4.1 继承](#841-继承)
        - [8.4.2 子类的构造函数](#842-子类的构造函数)
        - [8.4.2  将实例用作属性](#842--将实例用作属性)
    - [8.5 获取对象信息](#85-获取对象信息)
    - [8.6 实例属性和类属性](#86-实例属性和类属性)
    - [8.7 使用@property](#87-使用property)
    - [作业](#作业)

<!-- /TOC -->

## 8.1 简介
一个例子来说明面向过程与面向对象解决问题思维方式上的不同。
假设处理学生成绩表
- 面向过程的程序：
```python
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
```
处理学生成绩通过函数实现：
```python
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
```
- 面向对象的程序
们首选思考的不是程序的执行流程，而是```Student```这种数据类型应该被视为一个对象，这个对象拥有```name```和```score```这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个```print_score```消息，让对象自己把自己的数据打印出来。
```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
```
```python
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
```
在自然界中，**类（Class）** 和 **实例（Instance）** 的概念是很自然的。Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。

所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
面向对象的抽象程度比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
## 8.2 类和实例
### 8.2.1 类的定义和实例化
python中以class关键字定义类:
```python
class Student(object):
    pass
```
- 类名 通常以大写字母开始
- 父类(object，所有类都继承自这个类)
```python
bart = Student()
```
自由绑定属性
```python
bart.name = 'Bart Simpson'
print(bart.name)
```
### 8.2.2 构造函数

在创建实例的时候，把一些认为必须绑定的属性强制填写进去。通过定义一个特殊的```__init__```方法，在创建实例的时候，就把name，score等属性绑上去：
```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
```
- ```__init__```前后连个下划线
- ```self``` ：表示创建的实例本身(this)
```python
bart = Student('Bart Simpson', 59)

bart.name
# 'Bart Simpson'

bart.score
# 59
```
- 函数？方法？

和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。其他地方与函数完全一致。
### 8.2.3 数据封装
面向对象编程的一个重要特点就是数据封装.
```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bar = Student('Bart Simpson', 59)
bart.print_score();
```
这样一来，从外部看```Student```类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在```Student```类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节
## 8.3 访问控制 
上述代码中，看似将数据封装在class内部，但是，外部代码还是可以自由地修改一个实例的属性：
```python
bart = Student('Bart Simpson', 59)
bart.score
# 59

bart.score = 99
bart.score
# 99
```
HOWTO??

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线```__```, 变成私有变量。
```python
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 59)
bart.__name     # ArributeError
```
如果外部代码要获取```name```和```score```怎么办？可以给```Student```类增加```get_name```和```get_score```方法：
```python
class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
```

又要允许外部代码修改```score```怎么办？可以再给```Student```类增加```set_score```方法：
```python
class Student(object):
    ...

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
````

## 8.4 继承和多态
在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
### 8.4.1 继承
```python
class Animal(object):
    def run(self):
        print('Animal is running...')
```
```python
class Dog(Animal):
    pass

class Cat(Animal):
    pass
```
继承有什么好处？
- 获得父类功能
```python
dog = Dog()
dog.run()

cat = Cat()
cat.run()

Animal is running...
Animal is running...
```
- 多态
```python
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
```
关于多态的理解：子类对象给父类对象赋值或初始化(父类的引用对象指向子类的对象)。
```python
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
# Animal is running...
# Animal is running...

run_twice(Dog())
# Dog is running...
# Dog is running...

run_twice(Cat())
# Cat is running...
# Cat is running...
```
调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

- 对扩展开放：允许新增Animal子类；

- 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

### 8.4.2 子类的构造函数
创建子类的实例时, Python 首先需要完成的任务是给父类的所有属性赋值。为此,子类的方法 ```__init__()``` 需要父类施以援手。
```python
class Car():
    """ 一次模拟汽车的简单尝试 """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.modelreturn long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """ 电动汽车的独特之处 """
    def __init__(self, make, model, year):
    """ 初始化父类的属性 """
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```
给子类定义属性和方法：
```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
            电动汽车的独特之处
            初始化父类的属性,再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """ 打印一条描述电瓶容量的消息 """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()

# 2016 Tesla Model S
# his car has a 70-kWh battery.
```
### 8.4.2  将实例用作属性
```python

class Battery():
    """ 一次模拟电动汽车电瓶的简单尝试 """
    def __init__(self, battery_size=70):
        """ 初始化电瓶的属性 """
        self.battery_size = battery_size
    
    def describe_battery(self):
        """ 打印一条描述电瓶容量的消息 """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """ 电动汽车的独特之处 """
    def __init__(self, make, model, year):
        """
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```
## 8.5 获取对象信息
当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法?

- type()
它返回对应的Class类型。
```python
type(123)   # <class 'int'>
type('nxnu') # <class 'str'> 

type(123)==type(456)
# True

type('abc')==type('123')
# True

type(123)==int
# True

type('abc')==str
# True

type('abc')==type(123)
# False
```
type()函数适用于基本数据类型，要判断一个对象是否是函数怎么办？可以使用```types```模块中定义的常量：
```python
>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
```
- isinstance()
对于class的继承关系来说，使用type()就很不方便。要判断class的类型，可以使用isinstance()函数。
```python
object -> Animal -> Dog -> husky
```
```python
a = Animal()
d = Dog()
h = Husky()

isinstance(h, Husky)
# True

isinstance(h, Dog)
#True

isinstance(h, Animal)
# True

isinstance(d, Husky)
# False
```
同样isinstance()函数适用于基本类型：
```python
isinstance('a', str)
# True

isinstance(123, int)
# True

isinstance(b'a', bytes)
# True
```
另外，isinstance()函数还可以判断一个变量是否是某些类型中的一种：
```python
isinstance([1, 2, 3], (list, tuple))
# True

isinstance((1, 2, 3), (list, tuple))
# True
```

- dir()函数
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list.
```python
dir('nxnu')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

```python
__len__ 方法返回长度，调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__() 方法。自己写的类，如果也想使用len(myObj)，则需要实现一个 __len()__ 方法
```


```python
class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
len(dog)
# 100
```

配合getattr()、setattr()以及hasattr()，可以直接操作一个对象的状态：
```python
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
```

```python
hasattr(obj, 'x') # 有属性'x'吗？
# True
obj.x
# 9

hasattr(obj, 'y') # 有属性'y'吗？
#False

setattr(obj, 'y', 19) # 设置一个属性'y'

hasattr(obj, 'y') # 有属性'y'吗？
# True

getattr(obj, 'y') # 获取属性'y'
# 19

obj.y # 获取属性'y'
# 19
```

## 8.6 实例属性和类属性
由于Python是动态语言，根据类创建的实例可以任意绑定属性。
给实例绑定属性的方法是通过实例变量，或者通过self变量：
```python
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
```
但是，如果Student类本身需要绑定一个属性呢? 可以直接在class中定义属性，这种属性是类属性，归Student类所有
```python
class Student(object):
    name = 'Student'
```
定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到.
```python
s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student

print(Student.name) # 打印类的name属性
# Student

s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael

print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
# Student

del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student
```
- 实例属性属于各个实例所有，互不干扰；

- 类属性属于类所有，所有实例共享一个属性；

- 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误

## 8.7 使用@property

为了限制属性的取值范围，可以通过一个set_***()方法来设置成绩，再通过一个get_***()来获取成绩，这样，在set_***()方法里，就可以检查参数：
```python
class Student(object):
    
    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())
```
缺点：啰嗦、复杂

Python内置的@property装饰器就是负责把一个方法变成属性调用的：
```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，实际转化为s.get_score()
# 60
```

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

```python
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
```
## 8.8 多重继承
请自学，提问
## 作业
[慕课网-Python进阶](https://www.imooc.com/learn/317)