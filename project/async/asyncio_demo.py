import asyncio

@asyncio.coroutine
def hello():
    print('Hello World!')

    # 异步调用asyncio.sleep()
    # yield from 调用另外一个generator
    r = yield from asyncio.sleep(5)
    print(r)
    print('Hello Again!')

# 获取EvenLoop
loop = asyncio.get_event_loop()

# 执行corouting
loop.run_until_complete(hello())
loop.close()
'''
@asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。

hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
'''