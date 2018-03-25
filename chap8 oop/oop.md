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

## 8.6 实例属性和类属性