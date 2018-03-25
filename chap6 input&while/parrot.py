# input函数
#message = input('Tell me something, and I will repeat it back to you:')
#print(message)

"""
promt = 'If you tell us who you are, we can personalize the meesage you see.'
promt += '\nWhat is your first name?'
name = input(promt)
print('\nHello,' + name + '!')


promt = "\nTell me somethint, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(promt)

    if message != 'quit':
        print(message)

"""

promt = "\nTell me somethint, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(promt)
    if message == 'quit':
        active = False
    else:
        print(message)