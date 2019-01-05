def simple_coroutine(a):
    print('-> start ……')
    b = yield a
    print('-> 接收的参数为：', b)
    c = yield a+b
    print('-> 接收的参数：', c)
    print('-> end ……', a, b, c)


ct = simple_coroutine(5)

s1 = next(ct)
print(s1)
s2 = ct.send(3)
print(s2)
s3 = ct.send(2)
print(s3)

