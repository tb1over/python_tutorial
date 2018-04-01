from datetime import datetime

'''
def log(func):
    def wrapper(*args, **kw):
        print(' call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper;

# now = log(now)
@log
def now():
    print(datetime.now())

print(now.__name__)

now()

'''
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('excute')
def now():
    print(datetime.now())
print(now.__name__)
now()
