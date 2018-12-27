# -*- coding:utf-8 -*-

from python_high.com.python.demo.AthleteList import AthleteList
from python_high.com.python.demo.AthleteTest import sanitize


def get_coach_data(filename):
    try:
        with open('./chapter/' + filename) as file:
            data = file.readline().strip().split(',')
            return AthleteList(data.pop(0), data.pop(0), sorted(set([sanitize(d) for d in data]))[0:3])
    except IOError as error:
        print("file error:" + str(error))
        return None

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james.name + "'s faster time is: " + str(james))
print(julie.name + "'s faster time is: " + str(julie))
print(mikey.name + "'s faster time is: " + str(mikey))
print(sarah.name + "'s faster time is: " + str(sarah))