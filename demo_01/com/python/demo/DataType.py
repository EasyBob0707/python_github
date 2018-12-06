# 转义字符串中的双引号
print('I\'m \"OK\"!')
print('======================')
# 转义字符串中的换行
print('I\'m learning\nPython!')
# 字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
# 在命令行交互可以呈现效果，在文件中内容是以换行呈现的，那么打印的结果就是换行的形式(只需要在输出中有三对单引号)
print('''line1
line2
line3''')
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# >>> ord('A')
# 65
# >>> ord('中')
# 20013
# >>> chr(66)
# 'B'
# >>> chr(25991)
# '文'

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# x = b'ABC'

# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
# >>> 'ABC'.encode('ascii')
# b'ABC'
# >>> '中文'.encode('utf-8')
# b'\xe4\xb8\xad\xe6\x96\x87'
# >>> '中文'.encode('ascii')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# >>> b'ABC'.decode('ascii')
# 'ABC'
# >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# '中文'


# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
# >>> b'ABC'.decode('ascii')
# 'ABC'
# >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# '中文'

# 如果bytes中包含无法解码的字节，decode()方法会报错：

# >>> b'\xe4\xb8\xad\xff'.decode('utf-8')
# Traceback (most recent call last):
# ...
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：

# >>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
# '中'

# 要计算str包含多少个字符，可以用len()函数：

# >>> len('ABC')
# 3
# >>> len('中文')
# 2
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：

# >>> len(b'ABC')
# 3
# >>> len(b'\xe4\xb8\xad\xe6\x96\x87')
# 6
# >>> len('中文'.encode('utf-8'))
# 6

# 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，
# 要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写）
flag = True
print(flag)
# 布尔值可以用and、or和not运算
# 相当于java中的 &&、 || 和 !
print(not flag)
print(True or True)
print(True and not flag)
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值
# java中是null， scala中是Nothing

# 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
# 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量。
# 在Python中没有定义常量的关键字，只是有一个约定，常量名称必须大写，但是这样并不能实现让你不能修改数值
# 字符串也可以用单引号''引用
a = '123'
b = True
c = 'q'

# 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。
# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，
# 所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
PI = 3.1415926

# 整数的除法为什么也是精确的。在Python中，有两种除法，一种除法是/
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数, 整数的地板除//永远是整数，即使除不尽。
# 要做精确的除法，使用/就可以。因为//除法只取结果的整数部分。
print(10//3)
print(10/3)


