#!usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import reduce

def add(a, b):
    return a + b

print(add(1, 2))
print(add)

f = add
print(f)

# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。

# 成功！说明变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。
# 函数名也是变量
# 那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，
# 它指向一个可以计算绝对值的函数！
# 注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

# 传入函数, 将函数作为参数传入到函数中, 高阶函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(a, b, f):
    return f(a) + f(b)

print(add(-4, 3, abs))

# ======================高价函数之Map/Reduce======================
# Python内建了map()和reduce()函数。
# 把集合中的数据转换为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(a,b):
    return a + b

print(reduce(add, [1,2,3,4,5,6,7,8,9,10]))

def fn(a,b):
    return a * 10 + b

print(reduce(fn, [1,2,3,4,5,6,7]))

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def char2int(s):
    return DIGITS[s]

print(reduce(fn, map(char2int, "13579")))

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

def char2num(s):
    return DIGITS[s]

# lambda表达式进一步对代码进行优化
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# ======================高价函数之filter======================

def is_odd(x):
    return x % 2 != 0
# filter会作用到每一个元素上
print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 用filter求素数
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数。

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列




