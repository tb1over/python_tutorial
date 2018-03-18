<!-- TOC -->

- [1. 示例](#1-示例)
- [2. 条件测试](#2-条件测试)
    - [2.1 检查是否相等](#21-检查是否相等)
    - [2.2 检查是否不相等](#22-检查是否不相等)
    - [2.3 比较数字](#23-比较数字)
    - [2.4 检查多个条件](#24-检查多个条件)
    - [2.5 是否在/不在(in/not in)列表中](#25-是否在不在innot-in列表中)
    - [2.6 bool表达式](#26-bool表达式)
- [3. if语句](#3-if语句)
- [4. 检查特殊元素](#4-检查特殊元素)
- [5. 判断列表不为空](#5-判断列表不为空)
- [6. 多个列表](#6-多个列表)

<!-- /TOC -->
# 1. 示例
```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```
# 2. 条件测试
每条 if 语句的核心都是一个值为 True 或 False 的表达式,这种表达式被称为条件测试 。

## 2.1 检查是否相等
```python
car = 'bmw'
car == 'bmw'
```

## 2.2 检查是否不相等
```python
name = 'nxnu'
if name != 'sjxy':
    print('The name is : ' + name)
```

## 2.3 比较数字
相等、不相等、小于、小于等于、大于、大于等于

## 2.4 检查多个条件
- 逻辑与 and 
```python
age_0 = 22
age_1 = 18

age_0 >= 21 and age_1 >= 21


age_1 = 22

age_0 >= 21 and age_1 >= 21
```
- 逻辑或 or

## 2.5 是否在/不在(in/not in)列表中
```python
names = ['lucy', 'tom', 'jack', 'lili']
if 'hanmeimei' in names:
    print('OK!')
else:
    print('NO')

if 'html' not in names:
    print('html is not in the list') 
```
## 2.6 bool表达式
其实就是条件测试，结果为True 或者 false

# 3. if语句
```python
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```
```python
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
```
# 4. 检查特殊元素
```python
courses = ['html', 'css', 'javascript', 'python', 'go']
for course in courses :
    if 'go' == course:
        print('you have to study %s language next term'%course )
    else:
        print('you have to study ' + course + ' this term')
```

# 5. 判断列表不为空
```python
courses = []
if courses:
    for course in courses:
        print('course: ' + course)
else:
    print('you have nothing')
```

# 6. 多个列表
```python
available_skills = ['c', 'c++', 'java', 'javascript', 'html']
your_skills = ['eat', 'sleep']
for skill in your_skills:
    if skill not in available_skills:
        print('You must work hard to study more')
    else:
        print('Alread got the skill: ' + skill)
```