#!usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

file = ['How have you been? It had been quite some time since we last met.', "Nice to meet you C. I am A. I'm a psychology student.", 'Today is the last day of my final exam.', 'Yes. Do both of you have any plans for your holidays?', "It is very convenient then. I heard the accomodation there is very expansive. Since your sister is there then you don't need to worry much.", 'Have you found one?', 'Just like B, I am planning to go for a trip but I have not decide on which country to visit.', 'I was thinking about Thailand or Korea.', 'Yes I think so too. That is the reason why I have not make up my decision yet.', 'Bye. Take care.']


# 改造之前的代码输出格式
"""
该函数用于打印列表数据（支持嵌套列表）
改造函数可以将数据输出到文件当中
"""
def print_lol(lists, indent=False, level=0, fn=sys.stdout):
    """
    所打印出来的列表各占一行
    :param lists:   列表名称
    :param indent:  是否需要tab
    :param level:   tab个数
    :param fn:      写入文件对象
    :return: 直接打印列表数据
    """
    for li in lists:
        if isinstance(li, list):
            print_lol(li, indent, level + 1, fn)
        else:
            if indent:
                for stop in range(level):
                    print("\t", end='', file=fn)
            print(li, file=fn)


try:
    with open('./chapter/sys.txt', 'w') as sys:
        print_lol(file, fn=sys)
        sys.flush()
except IOError as error:
    print('file error' + str(error))
