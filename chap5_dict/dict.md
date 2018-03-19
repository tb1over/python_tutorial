# 1. 概述
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
```python
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
```
```python 
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
```
# 2. 原理
dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。

第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

# 3. 注意
和list比较，dict有以下几个特点：

- 查找和插入的速度极快，不会随着key的增加而变慢；
- 需要占用大量的内存，内存浪费多。

而list相反：

- 查找和插入的时间随着元素的增加而增加；
- 占用空间小，浪费内存很少。

需要牢记的一条就是dict的key必须是不可变对象。
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）

# 4. 使用字典

## 4.1 访问字典中的值
```python
alien_0 = {'color': 'green'}
print(alien_0['color'])
```

## 4.2 添加元素
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```
## 4.3 修改元素
```python
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
```
## 4.4 删除元素
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
```
# 5. 遍历字典
## 5.1 遍历所有的键值对
```python
user_0 = {
    'username': 'nxnu',
    'first': 'sjxy',
    'last': 'zhangsan',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
```

```python

favorite_languages = {
    'zs': 'python',
    'ls': 'c',
    'ww': 'ruby',
    'lucy': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")
```
## 5.2 遍历字典中的所有键
```python
favorite_languages = {
    'zs': 'python',
    'ls': 'c',
    'ww': 'ruby',
    'lucy': 'python',
}
for name in favorite_languages.keys():
    print(name.title())
```
## 5.3 遍历字典中所有的值
```python
favorite_languages = {
    'zs': 'python',
    'ls': 'c',
    'ww': 'ruby',
    'lucy': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```
注意上例中，value部分有重复值。可以使用set(集合).

# 6 集合(set)
**集合**类似于列表(字典)，但是每个元素必须独一无二
```python
favorite_languages = {
    'zs': 'python',
    'ls': 'c',
    'ww': 'ruby',
    'lucy': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

## 6.1 创建集合
要创建一个set，需要提供一个list作为输入集合：
```python
s = set([1, 2, 3])
s
# {1, 2, 3}
```
```python
s = set([1, 1, 2, 2, 3, 3])
s
# {1, 2, 3}
```
## 6.2 添加元素
```python
s.add(4)
```
## 6.3 删除元素
```python
s.remove(4)
```

## 6.4 数学运算
```python
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2 # {2, 3}
s1 | s2 # {1,2,3,4}
```
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素