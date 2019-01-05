def fun1():
    for i in 'abc':
        yield i


print(list(fun1()))


def fun2():
    yield from 'abc'


print(list(fun2()))


