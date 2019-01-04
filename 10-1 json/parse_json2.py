#!/usr/bin/env python
# coding=utf-8

import json


stu = {"name": "战国策", "age": 20, "sex": 1, "school": "清华大学"}

# help(json.dump)
with open('stu.json', 'w') as f:
    # ensure_ascii 中文字符是否需要转义
    json.dump(stu, f, ensure_ascii=True)

with open('stu.json', 'r') as f:
    res = json.load(f)
    print(type(res))
    print(res)
