# -*- coding:utf-8 -*-

import pickle

from python_high.com.python.demo.AthleteList import AthleteList

def sanitize(time_str):
    """
    将记录时间中的间隔符进行替换, 只保留.的形式
    :param time_str:    时间字符串
    :return:
    """
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return time_str
    (m, s) = time_str.split(splitter)
    return m + '.' + s

def get_coach_data(filename):
    """
    将用于读取文件使用
    :param filename:    将要读取的文件名称
    :return:
    """
    try:
        with open('./chapter/' + filename) as file:
            data = file.readline().strip().split(',')
            return AthleteList(data.pop(0), data.pop(0), sorted(set([d for d in data])))
    except IOError as error:
        print("file error:" + str(error))
        return None

def put_to_store(files_list):
    """
    定义一个字典数据类型, 将文件中的数据以二进制的形式存到文件当中
    :param files_list:  文件列表名称
    :return:            返回字典数据
    """
    all_athletes = {}
    for file in files_list:
        # 读取文件获取AthleteList对象
        ath = get_coach_data(file)
        # 将文件中的第一个数据（选手的姓名）作为字典数据的key, value则为整条数据
        all_athletes[ath.name] = ath
    try:
        with open('./chapter/allAthlete.txt', 'wb') as binary_file:
            pickle.dump(all_athletes, binary_file)
    except pickle.PickleError as error:
        print("pickle error is: " + str(error))

    return all_athletes

def get_from_store():
    """
    获取字典值的数据
    :return:    返回字典值的数据
    """
    all_athletes = {}
    try:
        with open('./chapter/allAthlete.txt', 'rb') as file:
            all_athletes = pickle.load(file)
    except pickle.PickleError as error:
        print("pickle error is: " + str(error))

    return all_athletes

# 测试以上的代码是否能够达到预想的效果
file_list = ['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
# 将文件放存入二进制文件中
allAthlete = put_to_store(file_list)
print(allAthlete)
# 从二进制文件中获取数据
getAllAthlete = get_from_store()
print(getAllAthlete)

# 注意：此处是map的循环
for athlete in getAllAthlete:
    print(getAllAthlete[athlete].name + ' ' + getAllAthlete[athlete].dob)


