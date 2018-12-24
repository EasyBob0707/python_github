#!usr/bin/env python3
# -*- coding:utf-8 -*-

import os

# 切换的文件的目录
os.chdir('./chapter')
# 查看当前所在的目录
print(os.getcwd())
# if os.path.exists("sketch.txt"):
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
            print(role, end='')
            print(" said:", end=' ')
            print(line_spoken, end='')
        except ValueError:
            # pass忽略这个错误
            pass
    open_file.close()
# else:
except IOError:
    print("file not exists!")