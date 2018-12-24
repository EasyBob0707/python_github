#!usr/bin/env python3
# -*- coding:utf-8 -*-

import os

# 验证Python异常处理场景
# 1、Python读取不到操作的文件
# 错误产生的原因： 获取读取的文件才存在文件的操作对象, 如果读取文件失败是没有文件对象的, 此时关闭文件对象就是有问题的
# 在Python的内置函数中存在local()函数, 该函数存放着当前作用域下的所有名的一个集合
# 关键字in不仅用于循环中, 还可以用于集合与个体之间的关系
try:
    test = open('test.txt')
    for t in test:
        print(t)
except IOError as error:
    # 无法获悉异常的具体信息
    print('file error：', error)
    print('file error：' + str(error))
    # 在Python中 + 号无法将对象转换成字符串的形式, 借助于str()函数完成
    # print('file error：' + error)
finally:
    if 'test' in locals():
        test.close()
    else:
        pass

# 验证in用于集合与个体之间的关系
L = [1,2,3,4,5]
print(1 in L)

A = []
B = []
# 尝试使用with关键字减少代码量
os.chdir('./chapter')
try:
    with open('test.txt') as test:
        for t in test:
            (role, line_spoken) = t.split(':')
            line_spoken = line_spoken.strip()
            if role == 'A':
                A.append(line_spoken)
            else:
                B.append(line_spoken)
except IOError as error:
    # 无法获悉异常的具体信息
    print('file error：', error)
    print('file error：' + str(error))
    # 在Python中 + 号无法将对象转换成字符串的形式, 借助于str()函数完成
    # print('file error：' + error)


# 尝试写文件
try:
    with open('testA.txt', 'w') as testA, open('testB.txt', 'w') as testB:
        print(A, file=testA)
        testA.flush()
        print(B, file=testB)
        testB.flush()
except IOError as error:
    print('file error' + str(error))
