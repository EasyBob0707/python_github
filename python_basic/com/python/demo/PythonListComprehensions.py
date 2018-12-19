#!usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import Iterator, Iterable

# Python中列表生成式
L = []
for x in range(1,11):
    L.append(x * x)
print(L[:])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([y for y in range(1,1000) if y % 2 != 0 and y % 3 != 0 and y % 5 != 0])

# 两层循环
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print({k + "=" + v for k,v in d.items()})

L = ['Hello', 'World', 'IBM', 'Apple']
print([l.lower() for l in L])
print([l.upper() for l in L])

# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()

g = (x * x for x in range(10))
print(g)
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
for j in g:
    print(j, end=" ")


# 普通的函数中如果带有yield关键字,那么该函数就不是一般的函数,而是generator
# 在执行流程上也有一定的差别,每次执行都是在上次执行的基础上继续向下执行

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

# 杨辉三角


# 迭代器
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象

# 判断集合是否可以迭代
print(isinstance([], Iterable))
# 判断元组是否可以迭代
print(isinstance((), Iterable))
# 判断字典是否可以迭代
print(isinstance({}, Iterable))
# 判断字符串是否可以迭代
print(isinstance("str", Iterable))
# 判断数字是否可以迭代
print(isinstance(100, Iterable))


print("============以下为可迭代的对象=============")

# 判断生成器是否为可迭代对象
print(isinstance((x for x in range(10)), Iterator))
# 判断元组是否为可迭代对象
print(isinstance((), Iterator))
# 判断字典是否为可迭代对象
print(isinstance({}, Iterator))
# 判断集合是否为可迭代对象
print(isinstance([], Iterator))
# 判断集合是否为可迭代对象
print(isinstance([], Iterator))

print("============将可迭代转换为可迭代对象=============")

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(()), Iterator))

# 你可能会问，为什么list、dict、str等数据类型不是Iterator?
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break