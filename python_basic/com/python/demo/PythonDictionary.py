#!usr/bin/env python3
# -*- coding:utf-8 -*-

# Python中字典的用法(相当于java中的map)

"""
该函数返回一个列表
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

def sanitize(time_str):
    """
    替换列表项中的数据
    :param time_str:    列表数据项的内容
    :return:
    """
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return time_str
    (mins, secs) = time_str.split(splitter)
    return (mins + '.' + secs)

dic = {}
james = get_coach_data("./chapter/james2.txt")
dic['name'] = james.pop(0)
dic['dob'] = james.pop(0)
dic['score'] = james
print(str(dic['name']) + "'s faster score is: " + str(sorted(set([sanitize(j) for j in dic['score']]))[0:3]))

"""
该函数返回一个字典
"""
def get_coach_data(file_name):
    """
    :param file_name:   文件名称
    :return:
    """
    try:
        with open(file_name) as file:
            # 返回一个去除空白并且用","分隔的字符串
            data = file.readline().strip().split(',')
            return {"name":data.pop(0), "dob":data.pop(0), "score":sorted(set([sanitize(d) for d in data]))[0:3]}
    except IOError as errors:
        print("file error:" + str(errors))
        return None


james2 = get_coach_data("./chapter/james2.txt")
julie2 = get_coach_data("./chapter/julie2.txt")
mikey2 = get_coach_data("./chapter/mikey2.txt")
sarah2 = get_coach_data("./chapter/sarah2.txt")
print(str(james2['name']) + "'s faster score is: " + str(james2['score']))
print(str(julie2['name']) + "'s faster score is: " + str(julie2['score']))
print(str(mikey2['name']) + "'s faster score is: " + str(mikey2['score']))
print(str(sarah2['name']) + "'s faster score is: " + str(sarah2['score']))