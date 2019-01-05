#!/usr/bin/env python
# coding=utf-8

import re

# match 从字符的起始位置匹配字符，若字符不在起始位置，则返回None
# 参数：
# pattern 正则模式（字符串）
# string 压迫匹配的字符串
# flag  标志 re.I：不区分大小写。re.L：本地化识别。re.M：多行匹配。re.S：是'.'好匹配换行符
res = re.match('www', 'www.baidu.com')
print(res)
res = re.match('baid', 'www.baidu.com')
print(res)


# search 扫描整个字符串，并返回第一个结果
# 参数：
# pattern 正则模式（字符串）
# string 压迫匹配的字符串
# flag  标志
res = re.search(r'\.\w', 'www.baidu.com')
print(res)
print(res.group(0))
print(res.groups())
print(res.span())

# sub 替换匹配内容
# 参数：
# pattern 正则模式（字符串）
# string1 替换的字符串|函数
# string2 要匹配的字符
# count 替换的次数，默认0，替换所有。
s = 'www.baidu.com'
res = re.sub(r'\.\w', '()', s,1)
print(res)


# 将匹配的字符输出两次
def str_double(matched):
    value = str(matched.group(0))
    return value*2


res = re.sub(r'\.\w', str_double, s, 1)
print(res)

print('*'*50)
# finditer 查找字符串中所有的匹配项，返回一个迭代器
# 参数
# pattern 正则表达式
# string 要匹配的字符串
# flag 标识
s = '123asdasdqwe12312asfqa134sdf234sd134'
res = re.finditer(r'[a-z]\d{2}', s)
for matched in res:
    print(matched)


print('-'*20)
# findall 查找字符串中的所有匹配项，返回一个列表
# 参数
# pattern 正则表达式
# string 要匹配的字符串
# flag 标识
res = re.findall(r'[a-z]\d{2}', s)
print(res)