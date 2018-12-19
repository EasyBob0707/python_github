#!usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数方法调用
# 数据类型转换
# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
import math

a = int("12345")
print(a)
b = int(123.456)
print(b)
f = float("12.345")
print(f)

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
x = a(-100)
print(x)

# ============================函数的定义=========================
def my_abs(num):
    if num >= 0:
        return num
    else:
        return -num

age = 18
if age >= 18:
    pass

# pass什么都不做只是一个占位符

# ============================参数检查=========================
def my_abs(num):
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')
    if num >= 0:
        return num
    else:
        return -num

# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。

# 解一元二次方程
def quadratic(a,b,c):
    p=b*b-4*a*c
    if p>=0 and a!=0:#一元二次方程有解的条件
        x1=(-b+math.sqrt(p))/(2*a)
        x2=(-b-math.sqrt(p))/(2*a)
        return x1,x2
    elif a==0:#a=0的情况下为一元一次方程
        x1=x2=-c/b
        return x1
    else:
        return('Wrong Number！')


# 计算未知数据的平方
def power(num):
    return num * num

# 计算未知数的n次方, 在定义函数的时候可以指定参数的默认值
def power(num, n=2):
    s = 1
    if n < 0:
        raise TypeError('bad index number')
    elif n == 0:
        return s
    elif n == 1:
        return num
    else:
        while True:
            s = s * num
            n = n - 1
            if n == 0:
                return s

h = power(2, 5)
print(h)

# 必选参数在前，默认参数在后，否则Python的解释器会报错
# 定义默认参数要牢记一点：默认参数必须指向不变对象!
# 调用多次会有多个数据被追加到可变对象当中
def add_end(L=[]):
    L.append("END")
    return L

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# ============================可变参数=========================
# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 可变参数如上述定义，在调用前需要先组合一个集合

# 为了方便调用，可以声明为如下的形式：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 不加*号也是可以的，加*表示以可变参数的形式传入
tu = (1,2,3,4,5,6,7,8)
l = [1,2,3,4,5,6,7,8]
calc(*tu)
calc(*l)

calc(1,2,3,4,5)

# ============================关键字参数=========================
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print("name: ", name, "age: ",age, "other: ", kw)

# 调用关键字函数
person("ZhangSan", 19, city="beijing", job="IT")

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

# ============================递归调用=========================
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(100))