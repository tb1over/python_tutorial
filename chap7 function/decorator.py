from datetime import datetime
import functools
'''
def log(func):
    @functools.wraps(func)
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
def logger(text):
    def decorator(func):
        #@functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logger('excute')
def now():
    print(datetime.now())
print(now.__name__)
now()
