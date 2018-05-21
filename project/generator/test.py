def f():
    print('start')
    a = yield 1 # 可以返回1，并接收传递的参数给a
    print('a=' + str(a) )

    print('middle')
    b = yield 2 # 可以返回2，并接收传递的参数给b
    print('b= ' + str(b) )

    print('next')
    c = yield 3 
    print('c= ' + str(c) )

gen = f()  # 不会执行，返回生成器
print(gen) # 打印出gen是个生成器对象

return1 = next(gen) # 执行生成器，停在第一个yield处，返回yield处的1给return1变量
# return1 = gen.send(None)  效果与上句相同
print(return1)

return2 = next(gen) # 执行生成器，将None传递给生成器中的a，返回yiled后的2
print(return2)

return3 = gen.send('msg') # 传入参数给b，返回3给,停在第三个yiled处
print(return3)

next(gen)  # 输出c的值为None，报错，遍历结束