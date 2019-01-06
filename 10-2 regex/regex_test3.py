#!/usr/bin/env python
# coding=utf-8

import re


# 匹配中文
# 大部分中文内容的表示范围是[\u4e00-\u9fa5]
s = u'你好，世界。 hello word!'
pt = re.compile(u'[\u4e00-\u9fa5]+')
rst = pt.findall(s)
print(rst)


# 贪婪和非贪婪
# '*'表示贪婪匹配，'?'表示非贪婪匹配
s = '<div>这是div1</div><p></p><div><span>这是div2，被span包着</span></div>'
# 贪婪匹配
pat1 = re.compile(r'(<div>.*</div>)+')
# 非贪婪匹配
pat2 = re.compile(r'(<div>.*?</div>)+')

res1 = pat1.search(s)
print(res1)
print(res1.group(0))

res2 = pat2.findall(s)
print(res2)

