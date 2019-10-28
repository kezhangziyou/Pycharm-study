# 0-如何定义一个函数
"""
定义一个函数有如下几个步骤
1.函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
2.任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。
不带表达式的return相当于返回 None。
语法
def 函数名（参数列表）:
    函数体
默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
"""

# 1-定义一个无参函数
import math


def hello():
    # 定义一个函数
    print("Hello World!")


# 调用函数
print("调用无参函数:", hello())


# 2-定义一个条件函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print("88的绝对值:", my_abs(-88))


# 3-定义一个有参数函数
def helloName(name):
    print("Hello World!", name)


# 调用函数
print("调用有参函数:", helloName(' python'))


# 4-定义函数
def add(a, b):
    return a + b


def reduce(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("1+2=", add(1, 2))
print("12-2=", reduce(12, 2))
print("6*3=", multiply(6, 3))
print("12/6=", divide(12, 6))


# 5-定义多个返回值函数
def more(x, y):
    nx = x + 2
    ny = y - 2
    return nx, ny


# 调用函数
x, y = more(10, 10)
print(x, y)

"""
比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标
"""


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
"""
但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。"""
r = move(100, 100, 60, math.pi / 6)
print(r)

# 6-定义一个递归函数
"""
所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(6))  # 720

# 7-调用官方的函数
print(abs(-99))
"""
sum()函数接受一个list作为参数，并返回list所有元素之和。
请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
"""


def sum(n):
    return n * n


L = [1, 2, 3]
count = 0
for i in range(len(L)):
    count = count + sum(L[i])

print(count)

# 8-函数-默认参数,由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面：
"""
例如Python自带的 int() 函数，其实就有两个参数，我们既可以传一个参数，又可以传两个参数：
 OK:
def fn1(a, b=1, c=2):
    pass
 Error:
def fn2(a=1, b):
    pass

"""
print("十进制的123:", int('123'))
print("八进制的123:", int('123', 8))


def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print("3的4次方:", power1(3, 4))


def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print("5的平方:", power2(5))

# 9-Python之定义可变参数
"""
如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数

Python之定义可变参数
如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数：
def fn(*args):
    print args
可变参数的名字前面有个 * 号，我们可以传入0个、1个或多个参数给可变参数：
"""


def fn(*args):
    print(args)


fn()
fn('a')
fn('a', 'b')
fn('a', 'b', 'c')


# 计算任意个数的平均值，就可以定义一个可变参数：
def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)


print("无参数的平均数", average())
print("1,2的平均数", average(1, 2))
print("1, 2, 2, 3, 4的平均数", average(1, 2, 2, 3, 4))
