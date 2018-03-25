<!-- TOC -->

- [chapt7](#chapt7)
    - [7.1 函数input](#71-函数input)
    - [7.2 while循环](#72-while循环)
    - [7.3使用while循环处理列表和字典](#73使用while循环处理列表和字典)

<!-- /TOC -->

# chapt7

## 7.1 函数input
input()函数让程序暂停执行，等待用户输入一些文本。获取输入之后,Python将其存储在一个变量中.
```python
message = input('Tell me something, and I will repeat it back to you:')
print(message)
```

- 提示清晰
```python
promt = 'If you tell us who you are, we can personalize the meesage you see.'
promt += '\nWhat is your first name?'
name = input(promt)
print('\nHello,' + name + '!')
```
- 使用input来获取数值输入
```python
age = input('How old are you?')
age = int(age)
```
- 求模运算符
```python
# even_or_add.py

```

## 7.2 while循环
for循环用于针对集合中的每个元素的一个代码块，而while循环不断地运行，直到指定的条件不满足为止
- 使用while
```python
# counting.py
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

- 用户选择何时退出
```python
#  parrot.py
promt = "\nTell me somethint, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(promt)

    if message != 'quit':
        print(message)
```

- 使用标志
可以使用boolean类型的变量作为标志，注意boolean类型取值为True, False
```python
#   parrot.py
promt = "\nTell me somethint, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(promt)
    if message == 'quit':
        active = False
    else:
        print(message)
```
- break退出循环
break作用于其他语言中的作用一致
```python
#  cities.py
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished)"

while True:
    city = input(prompt)

    if(city == 'quit'):
        break
    else:
        print("I'd love to go to " + city.title() + " !")
```
- continue
continue与其他语言中作用类似
```python
# counting.py
```

- 避免无限循环
```python
x = 1
while x < 5 :
    print(x)
```

## 7.3使用while循环处理列表和字典
for循环中不应该来修改列表或字典，否则python无法跟踪其中的元素。要在遍历列表时对其修改，可使用while
- 在列表之间移动元素
```python
# confirmed_users.py
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user:" + current_user.title())

    confirmed_users.append(current_user)

# 显示已经验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

- 删除包含特定值的所有列表元素
使用remove函数来删除列表中的特定值
```python
# pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

- 使用用户输入来填充字典
```python
# mountain_poll.py
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhich is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
```