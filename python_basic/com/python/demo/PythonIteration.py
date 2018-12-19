#!usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import Iterable

# 集合迭代
L = list(range(100))
S = set([1,2,3,4,5,6,7,8])

for l in L:
    print(l, end=" ")
print()

for s in S:
    print(s, end=" ")
print()


# 元组的迭代
T = (1,2,3,4,5,6,S)
for t in T:
    print(t, end=" ")
print()

# 字典迭代
D = {"key01":"value01","key02":"value02","key03":"value03"}

for value in D.values():
    print(value, end=" ")
print()

for k,v in D.items():
    print(k,v, end=" ")
print()

# 判断字符串是否属于可迭代的
print(isinstance('abc', Iterable))
