#!usr/bin/env python3
# -*- coding:utf-8 -*-

import pickle

# 用pickle数据处理引擎处理数据(运用二进制的方式处理数据)压缩
try:
    with open('./chapter/myData.txt', 'wb') as data:
        pickle.dump([1,2,'three','four','five'], data)
except pickle.PickleError as error:
    print("pickle error" + str(error))

try:
    with open('./chapter/myData.txt', 'rb') as data:
        l = pickle.load(data)
        print(l)
except pickle.PickleError as error:
    print("pickle error" + str(error))
