import hashlib, random

db1 = {}

def register(username, password):
    db1[username] = User(username, password)

def get_md5(s):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username        # chr() 返回对应的字符
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(username + password + self.salt)

def login(username, password):
    user = db1[username]
    return user.password == get_md5(username + password + user.salt)

register('michael', '123456')
register('bob', 'abc999')
register('alice', 'alice2008')

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')