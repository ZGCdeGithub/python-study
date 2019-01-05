import re


#compile 编译正则表达式，生成一个正则对象
# 参数
# pattern 正则字符串
# flag 标识符

pat = re.compile('\d{3}')
s = 'wqa123asd23dasd324asd1232234'
res = pat.search(s, 0, 10)
print(res)
print(res.span())
print(res.group(0))
print(res.start(), res.end())


# match 和search只要匹配一个就不会再进行匹配
# 若想匹配多个结果，使用findall
# findall 查找多个匹配
# 参数：
# string 要匹配的字符串
# startP 从什么位置开始匹配（可选，包括该位置）
# endP 到什么位置结束匹配（可选，不包括该位置）
# 返回的是一个列表
pat = re.compile('\d{3}')
res = pat.findall(s)
print(res)
# print(res.group())
