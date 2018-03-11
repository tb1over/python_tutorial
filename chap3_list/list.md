<!-- TOC -->

- [1 列表是什么](#1-列表是什么)
    - [1.1 访问列表元素](#11-访问列表元素)
    - [1.2 索引从0开始](#12-索引从0开始)
    - [1.3 使用列表中的额各个值](#13-使用列表中的额各个值)
- [2. 修改、添加、删除元素](#2-修改添加删除元素)
    - [2.1 修改元素](#21-修改元素)
    - [2.2 添加元素](#22-添加元素)
    - [2.3 删除元素](#23-删除元素)
- [3. 组织列表](#3-组织列表)
    - [3.1永久排序](#31永久排序)
    - [3.2 临时排序](#32-临时排序)
    - [3.3 反转列表](#33-反转列表)
    - [3.4列表长度](#34列表长度)
- [4. 列表操作](#4-列表操作)
    - [4.1 遍历链表](#41-遍历链表)
    - [4.2 创建数值列表](#42-创建数值列表)
    - [4.3 切片](#43-切片)
    - [4.5 元组](#45-元组)

<!-- /TOC -->

# 1 列表是什么
**列表**由一系列按特定顺序排列的元素组成。可以将任何东西加入列表中,其中的元素之间可以没有
任何关系。

在 Python 中,用方括号( [] )来表示列表,并用逗号来分隔其中的元素
```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```
## 1.1 访问列表元素
列表是有序集合,因此要访问列表的任何元素,只需将该元素的位置或索引告诉 Python 即可。要访问列表元素,可指出列表的名称,再指出元素的索引,并将其放在方括号内。
```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```
## 1.2 索引从0开始
```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
```
Python 为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为 -1
```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
# -2, -3 ....
```
## 1.3 使用列表中的额各个值
```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
```

# 2. 修改、添加、删除元素
创建的大多数列表都将是动态的,这意味着列表创建后,将随着程序的运行增删元素.
## 2.1 修改元素
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```
## 2.2 添加元素
- 在列表尾部添加元素
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# or
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
```
- 在列表中插入元素
```py
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
```
## 2.3 删除元素
- del 语句删除元素
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
```
- pop()方法删除
有时候,要将元素从列表中删除,并接着使用它的值.方法 pop() 可删除列表末尾的元素,并让你能够接着使用它.
```py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()

print(motorcycles)
print(popped_motorcycle)
```
- 弹出列表中任意位置元素
使用 pop() 来删除列表中任何位置的元素,只需在括号中指定要删除的元素的索引即可
```py
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)

print('The first motorcycle I owned was a ' + first_owned.title() + '.')
```
- 根据值删除元素
有时候,不知道要从列表中删除的值所处的位置。如果只知道要删除的元素的值,可使用方法 remove()
```py
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
```

```py
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
```
**注意**方法 remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次,就需要使用循环来判断是否删除了所有这样的值。

# 3. 组织列表
## 3.1永久排序

```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars) #['toyota', 'subaru', 'bmw', 'audi']
```
## 3.2 临时排序
要保留列表元素原来的排列顺序,同时以特定的顺序呈现它们,可使用函数 sorted().
```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
```
## 3.3 反转列表
可使用方法 reverse()
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #永久修改cars
print(cars)
```
## 3.4列表长度
```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
```

# 4. 列表操作
## 4.1 遍历链表
```py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```
关于for循环需要注意以下几点：
- 缩进问题
- 冒号
- for .... in .... :


## 4.2 创建数值列表　
Python 提供了很多工具,可帮助高效地处理数字列表。
- range()函数
```py
for value in range(1,5):
    print(value)
```
- 创建数字列表
```py
numbers = list(range(1,6))
print(numbers)
```
```py
# 指定步长
even_numbers = list(range(2,11,2))
print(even_numbers)
```
使用函数 range() 几乎能够创建任何需要的数字集,例如,如何创建一个列表,其中包含前 10 个整数(即 1~10 )的平方呢?
```py
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
```
- 数字列表简单统计
```py
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)
```
- 列表解析
列表解析 将 for 循环和创建新元素的代码合并成一行,并自动附加新元素.
```py
squares = [value**2 for value in range(1,11)]
print(squares)
```
## 4.3 切片
切片对列表的操作非常方便，使用非常频繁。要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) 
# ['charles', 'martina', 'michael']

print(players[1:4])
# ['martina', 'michael', 'florence']

print(players[:4])
# ['charles', 'martina', 'michael', 'florence']

print(players[2:])
# ['michael', 'florence', 'eli']

print(players[-3:])
# ???

for player in players[:3]:
    print(player.title())
# ???

```
**复制列表：**
```py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
**注意：**
```py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
```py
my_foods = ['pizza', 'falafel', 'carrot cake']
# 注意这里
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

```
## 4.5 元组