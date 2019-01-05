def simple_coroutine():
    print(' start ……')
    x = yield
    print('接收的x是：', x)
    print('end ……')


ct = simple_coroutine()
# 使用next调用，真正开始执行
next(ct)
# 也可以使用ct.send(None)调用，与next()效果一样
# ct.send(None)

# 使用send(),并传入参数,yield处开始执行，并将传入的参数赋值给yield左边等号的左边
ct.send(10)

