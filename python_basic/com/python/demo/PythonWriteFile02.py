#!usr/bin/env python3
# -*- coding：utf-8 -*-

import os, pickle

A = []
B = []
J1 = []
J2 = []
K = []

# 切换的文件的目录
os.chdir('./chapter')
# 查看当前所在的目录
print(os.getcwd())
try:
    open_file = open("sketch.txt")
    # 打印文件对象, 该对象是可以进行迭代的
    print(open_file)
    for data in open_file:
        try:
            # 检查字符串中是否存在分号:,没有分号返回-1,有分号返回分号:的下标
            # if not data.find(':') == -1: # data.find(':') != -1:
            # 如果字符串中有多个分号：,那么只有第一个分号是生效的（可以将下面的理解成把数据切分几次）
            (role, line_spoken) = data.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'A':
                A.append(line_spoken)
            elif role == 'B':
                B.append(line_spoken)
            elif role == 'J1':
                J1.append(line_spoken)
            elif role == 'J2':
                J2.append(line_spoken)
            else:
                K.append(line_spoken)
        except ValueError:
            # pass忽略这个错误
            pass
    open_file.close()
except IOError:
    print("file not exists!")


try:
    with open("ab.txt", 'wb') as a, open("bb.txt", 'wb') as b, open("j1b.txt", 'wb') as j1, open("j2b.txt", 'wb') as j2, open("kb.txt", 'wb') as k:

        pickle.dump(A, a)
        pickle.dump(B, b)
        pickle.dump(J1, j1)
        pickle.dump(J2, j2)
        pickle.dump(K, k)

except pickle.PickleError as error:
    print("Pickle IOException:" + str(error))

