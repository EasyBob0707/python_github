#!usr/bin/env python
# -*- coding:utf-8 -*-

import os

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

def sanitize(time_str):
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return time_str
    (mins, secs) = time_str.split(splitter)
    return (mins + '.' + secs)

james_data = get_coach_data('./chapter/james2.txt')
(name, bro) = james_data.pop(0), james_data.pop(0)
print(name + "'s faster score :" + str(sorted(set([sanitize(j) for j in james_data]))[0:3]))