#!usr/bin/env python3
# -*- coding:utf-8 -*-

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

