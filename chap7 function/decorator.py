from datetime import datetime

def log(func):
    def wrapper(*args, **kw):
        print(' call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper;

@log
def now():
    print(datetime.now())

# now = log(now)
print(now.__name__)

now()