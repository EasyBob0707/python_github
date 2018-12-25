#!usr/bin/env python3
# -*- coding:utf-8 -*-

import os

# Python处理非格式统一的数据
"""
封装读取文件内容的方法
"""
def get_coach_data(file_name):
    """
    :param file_name:   文件名称
    :return:
    """
    try:
        with open(file_name) as file:
            # 返回一个去除空白并且用","分隔的字符串
            return file.readline().strip().split(',')
    except IOError as errors:
        print("file error:" + str(errors))
        return None

os.chdir('./chapter')
try:
    with open('james.txt') as james, open('julie.txt') as julie, open('mikey.txt') as mikey, open('sarah.txt') as sarah:
        james = james.readline().strip().split(',')
        julie = julie.readline().strip().split(',')
        mikey = mikey.readline().strip().split(',')
        sarah = sarah.readline().strip().split(',')
except IOError as error:
    print("file error:" + str(error))

print(james)
print(julie)
print(mikey)
print(sarah)


# 格式化数据的函数
def sanitize(time_str):
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return time_str
    (mins, secs) = time_str.split(splitter)
    return (mins + '.' + secs)

james_sort = []
julie_sort = []
mikey_sort = []
sarah_sort = []

for j in james:
    james_sort.append(sanitize(j))
for ju in julie:
    julie_sort.append(sanitize(ju))
for m in mikey:
    mikey_sort.append(sanitize(m))
for s in sarah:
    sarah_sort.append(sanitize(s))

print(sorted(james_sort))
print(sorted(julie_sort))
print(sorted(mikey_sort))
print(sorted(sarah_sort))

# 简写(隐含使用集合追加append())
# james_sort = [sanitize(j) for j in james]

# 上述代码精简
print(sorted([sanitize(j) for j in james]))
print(sorted([sanitize(j) for j in julie]))
print(sorted([sanitize(j) for j in mikey]))
print(sorted([sanitize(j) for j in sarah]))

# 去除重复的数据项
james_repeat = []
julie_repeat = []
mikey_repeat = []
sarah_repeat = []

for j in sorted(james_sort):
    if j not in james_repeat:
        james_repeat.append(j)
for ju in sorted(julie_sort):
    if ju not in julie_repeat:
        julie_repeat.append(ju)
for m in sorted(mikey_sort):
    if m not in mikey_repeat:
        mikey_repeat.append(m)
for s in sorted(sarah_sort):
    if s not in sarah_repeat:
        sarah_repeat.append(s)

print(james_repeat[0:3])
print(julie_repeat[0:3])
print(mikey_repeat[0:3])
print(sarah_repeat[0:3])


# 精简重复数据的代码
# 用set()函数自身的优势直接就可以去除重复的数据
print(sorted(set(james_sort))[0:3])
print(sorted(set(julie_sort))[0:3])
print(sorted(set(mikey_sort))[0:3])
print(sorted(set(sarah_sort))[0:3])