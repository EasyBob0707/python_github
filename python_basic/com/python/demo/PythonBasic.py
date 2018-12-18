#!usr/bin/env python3
# -*- coding: utf-8 -*-

# Python中List集合与元组
# 定义集合使用中括号[], 定义元组使用小括号().
# 集合可以插入数据,更新数据;但是元组中的数据是不可变的
# 访问数据的方式都是一致的,通过中括号[]进行访问数据

# ============================判断语句=========================

# 系统等待输入
# age = int(input('age:'))
age = 90
if age < 18:
    print("未成年")
elif 18 < age < 60:
    print("已成年")
elif age > 60:
    print("老年人")

# end=""是打印不换行的操作

# ============================循环语句=========================

# 遍历集合
classmates = ['Michael', 'Bob', 'Tracy']
for cla in classmates:
    print(cla + " ", end="")

print()

# 遍历元组
names = ('Michael', 'Bob', 'Tracy')
for name in names:
    print(name + " ", end="")

print()

# 从1累加到1000
# 在Python中使用range()方法可以达到目的
# range()方法是可以生成序列的一个方法
# 比如range(5)通过list()之后生成的数据是从0到4
# list()方法可以将整数序列转换成list集合
lists = list(range(101))
s = 0
for li in lists:
    s += li
print(s)
lis = []
# Python中break与continue的用法是一样的
for n in list(range(11)):
    if n % 2 == 0:
        lis.append(n)
    else:
        continue

print(lis)

n = 11
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')


# 循环是让计算机做重复任务的有效的方法。
# break语句可以在循环过程中直接退出循环，
# 而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
# 这两个语句通常都必须配合if语句使用。
# 要特别注意，不要滥用break和continue语句。
# break和continue会造成代码执行逻辑分叉过多，容易出错。
# 大多数循环并不需要用到break和continue语句，
# 上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

# ============================字典数据类型=========================

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# Python中的dist字典数据类型就是其他语言中的map
# Python中声明dict数据类型用大括号{}

# 可以声明重复的key,但是只显示一个
d = {"key01": "value01", "key01" : "value01"}
print(d["key01"]) # value01
print(len(d))  # 长度是1


# 把数据放入到d中
d["key02"] = "value02"
print(len(d))
print(d["key02"])


# Python中获取dict中不存在的key会报异常
# print(d["aaa"])
# 可以用in来判断key是否存在于dict中
if "aaa" in d:
    print(True)
else:
    print(False)


# 还可以通过dict的get()方法来获取value数据
# 这样做的好处是：如果不存在不会报异常,返回None
print(d.get("aaa"))

# 要删除可以使用pop(),可以从dict中获取数据并且从数据源中删除
print(d.pop("key02"))
# 同样可以自己定pop()返回的数据
print(d.pop("key02", -1))
print(len(d))

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
# 这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
# 而list是可变的，就不能作为key
keys = [1,2,3]
# d = {keys, "123"}
# list集合是可变的数据类型，不能作为dict的key

# ============================set数据类型=========================

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# Python中的set集合与Java中的set集合,不可重复的一组数据
# Python中定义set集合：set([1,2,3])
ks = set([1,2,3,4,5,6,7,8])
print(ks)
ks.add(9)
print(ks)
for k in ks:
    print(k, end="  ")
print()

ks.remove(5)
for k in ks:
    print(k, end="  ")
print()

# ks.add(lis)
# 不能加入list集合数据






