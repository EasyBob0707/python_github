#!usr/bin/env python3
# -*- coding:utf-8 -*-

"""
该函数用于打印列表数据（支持嵌套列表）
"""
def print_lol(lists):
    """
    所打印出来的列表各占一行
    :param lists: 列表名称
    :return: 直接打印列表数据
    """
    for li in lists:
        if isinstance(li, list):
            print_lol(li)
        else:
            print(li)

L = list(range(1, 10))
Li = list(range(1, 5))
Li.append(L)

print(print_lol(Li))


"""
该函数用于打印列表数据（支持嵌套列表）
"""
def print_lol(lists, indent=False, level=0):
    """
    所打印出来的列表各占一行
    :param lists: 列表名称
    :param indent: 是否需要tab
    :param level: tab个数
    :return: 直接打印列表数据
    """
    for li in lists:
        if isinstance(li, list):
            print_lol(li, indent, level + 1)
        else:
            if indent:
                for stop in range(level):
                    print("\t", end='')
            print(li)

print(print_lol(Li, True))