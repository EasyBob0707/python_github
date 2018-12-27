# -*- coding:utf-8 -*-

from python_high.com.python.demo.Athlete import Athlete

def sanitize(time_str):
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return time_str
    (mins, secs) = time_str.split(splitter)
    return (mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open('./chapter/' + filename) as file:
            data = file.readline().strip().split(',')
            return Athlete(data.pop(0), data.pop(0), sorted(set([sanitize(d) for d in data]))[0:3])
    except IOError as error:
        print("file error:" + str(error))
        return None


james = Athlete('James', '2002-6-12', ['2.01', '2.22', '2.34'])
sarah = Athlete('Sarah')

print(type(james))
print(type(sarah))

print(james.name)
print(james.dob)
print(james.time)

james = get_coach_data('james2.txt')
print(james.name + "'s faster time is :" + str(james.time))


vera = Athlete('Vera vi')
vera.add_time('3.66')
vera.add_times(['2.13','2.67'])
print(vera.name + "'s time is :" + str(vera.time))