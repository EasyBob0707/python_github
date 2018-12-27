# -*- coding:utf-8 -*-
from python_high.com.python.demo.NameList import NameList

john = NameList('John')

# 查看类中的有哪些可以操作的方法
print(dir(john))
print(type(john))
print(john.name)
john.append('Bass Player')
john.extend(['Composer','Arranger','Musician'])
print(john)
print(john.name)

for j in john:
    print('John is a ' + j + '.')

