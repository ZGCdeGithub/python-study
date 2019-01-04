#!/usr/bin/env python
# coding=utf-8

import re

# match 从字符的起始位置匹配字符，若字符不在起始位置，则返回None
res = re.match('www', 'www.baidu.com')
print(res)
res = re.match('baid', 'www.baidu.com')
print(res)


