#!usr/bin/env python3
# -*- coding:utf-8 -*-

# Python排序：原地排序和复制排序

L = [1,3,4,2,5,9,7,5,3,2,1]

# 复制排序：将原集合复制一份, 对复制的集合进行排序, 不影响原集合的顺序
# print(L)
# print(sorted(L))

# 原地排序：对原有的集合进行排序
L.sort()
print(L)