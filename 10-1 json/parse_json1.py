#!/usr/bin/env python
# coding=utf-8

import json


# string、int、bool、None转换
s = 'abcdefg'
print(json.dumps(s))

i = 123
print(json.dumps(i))

b = True
print(json.dumps(b))

n = None
print(json.dumps(n))

stu = {'name': '战国策', 'grade': '9', 'manage': 'Mr wang'}
print(type(stu))
print(stu)

# 字典转换成json字符串
stu_json = json.dumps(stu)
print(type(stu_json))
print(stu_json)

# 将json字符串转换成python对象
json_str = '{"code":0, "msg":"success","referer":"http://baidu.com","webname":"百度一下"}'
d1 = json.loads(json_str)
print(type(d1))
print(d1)


# list对象转换
l = [1, 'abc', True, -99, None]
l_json = json.dumps(l)
print(type(l_json))
print(l_json)

# tuple对象转换
t = (1,123,'abc',False)
print(json.dumps(t))

# set对象转换,不可转换
# s = {1,99,'rbc',None}
# print(json.dumps(s))

