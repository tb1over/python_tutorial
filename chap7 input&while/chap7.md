##7.1 函数input
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