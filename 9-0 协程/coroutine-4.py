from collections import namedtuple

ResClass = namedtuple('Res', 'count average')


# 子生成器
def average():
    total, count, average = 0, 0, None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return ResClass(count, average)


# 委派生成器
def grouper(storages, key):
    while True:
        storages[key] = yield from average()


# 客户端代码
def client():
    process_data = {
        'boy_1': [39.2, 45.8, 78.2, 12.5, 62.0, 38.5, 90.2],
        'boy_2': [10.2, 20.3, 30.4, 40.5, 50.6, 60.7, 70.8]
    }
    storages = {}
    for k, v in process_data.items():
        # 获得协程
        coroutine = grouper(storages, k)

        # 预激协程
        next(coroutine)

        # 想协程发送数据
        for val in v:
            coroutine.send(val)

        # 终止协程
        coroutine.send(None)
    print(storages)


client()
