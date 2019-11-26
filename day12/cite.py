from sys import getrefcount

"""
1. 引用简介与工具引入
Python 中对于变量的处理与 C 语言有着很大的不同，Python 中的变量具有一个特殊的属性：
identity，即“身份标识”。这种特殊的属性也在很多地方被称为“引用”。

为了更加清晰地说明引用相关的问题，我们首先要介绍两个工具：一个Python的内置函数：id()；
一个运算符：is；同时还要介绍一个sys模块内的函数：getrefcount()。
"""

"""
1.1 内置函数id()
id(object):
        返回值为传入对象的“标识”。该标识是一个唯一的常数，在传入对象的生命周期内与之一一对应。
        生命周期没有重合的两个对象可能拥有相同的id()返回值。

CPython 实现细节：“标识”实际上就是对象在内存中的地址。
换句话说，不论是否是 Python 实现，一个对象的id就可以视作是其虚拟的内存地址。

"""

"""
1.2 运算符is
即is的作用是比较对象的标识。
"""

"""
1.3 sys模块函数getrefcount()函数 
sys.getrefcount(object)返回值是传入对象的引用计数。由于作为参数传入getrefcount()的时候产生了
一次临时引用，因此返回的计数值一般要比预期多1。
此处的“引用计数”，在 Python 文档中被定义为“对象被引用的次数”。一旦引用计数归零，则对象所在的内存被释放。
这是 Python 内部进行自动内存管理的一个机制,相当于 java 的引用计数内存回收机制.
"""
const_ref1 = 10000
print("const_ref1变量的引用次数getrefcount(const_ref1):", getrefcount(const_ref1))

# 问题示例
"""
C 语言中，变量代表的就是一段固定的内存，而赋给变量的值则是存在这段地址中的数据；但对 Python 来说，
变量就不再是一段固定的地址，而只是 Python 中各个对象所附着的标签。理解这一点对于理解 Python 的很多特性十分重要。


2.1 对同一变量赋值
对于如下的 c 语言代码
int c_variable = 10000;
printf("original address: %p\n", &a); // original address: 0060FEFC
c_variable = 12345;
printf("second address: %p\n", &a); // second address: 0060FEFC
变量c_variable的地址并不会因为赋给它的值有变化而发生变化。对于 C 编译器来说，
变量c_variable只是协助它区别各个内存地址的标识，是直接与特定的内存地址绑定的，
python是完全不一样的
"""
python_variable = 10000
print(id(python_variable))  # 4340678544
python_variable = 12345
print(id(python_variable))  # 4340678288

python_variable = 10000
print(id(python_variable))  # 4340678544

python_variable1 = [1, 2]
print(id(python_variable1))  # 1823863879824
python_variable1 = [1, 2]
print(id(python_variable1))  # 1823863880176

# Python在内存中维护了一个特定数量的常量池，
"""
Python在内存中维护了一个特定数量的常量池，对于一定范围内的数值均不再创建新的对象，
而直接在这个常量池中进行分配。实际上在我的机器上使用如下代码可以得到这个常量池的范围是 
[0, 256] ，而 256 刚好是一个字节的二进制码可以表示的值的个数。

"""

for constant in range(300):
    if constant is not range(300)[constant]:
        print("常量池最大值为：", (constant - 1))
        break
# 常量池最大值为： 256

# 下面三个的id值都是一样的
littleConst = 1  # 数值较小的整型对象
print(id(littleConst))  # 4305222016
littleConst = 1
print(id(littleConst))  # 4305222016
140734357607232
print(id(1))  # 4305222016

#  数值进行加减乘除并将结果赋给原来的变量，都会改变变量对应的引用值
"""

"""
change_ref = 10000
print("id(change_ref)的原始的id值:", id(change_ref))
print("change_ref", change_ref)
change_ref = change_ref + 1  # 相加得到了一个新的树枝,其引用也随之改变
print("change_ref", change_ref)
print("id(change_ref)的相加后的id值:", id(change_ref))

# 对于 list 会不变
"""
list 是可变对象
"""

list_nonchange = [1, 2, 3]
print("id(list_nonchange)", id(list_nonchange))

2161458355400
list_nonchange[2] = 5
print("id(list_nonchange)", id(list_nonchange))

list_nonchange.append(3)
print(list_nonchange)
print(id(list_nonchange))

# 浅拷贝的原理解析
list_example = [1, 2, 3]
list_same_ref = list_example
print("id(list_example):", id(list_example))
print("id(list_same_ref):", id(list_same_ref))
# 改变原值,新值也会改变,但是相对应元素的引用均没有改变
list_example[2] = 5
print("id(list_example):", id(list_example))
print("id(list_same_ref):", id(list_same_ref))
list_example.append(3)
print("id(list_example):", id(list_example))
print("id(list_same_ref):", id(list_same_ref))
del list_example[3]
print("id(list_example):", id(list_example))
print("id(list_same_ref):", id(list_same_ref))

# 特殊情况
"""
加法运算符在 Python 中存在重载的情况，对列表对象和数值对象来说，加法运算的底层实现是完全不同的，
在简单的加法中，列表的运算还是创建了一个新的列表对象；但在简写的加法运算+=实现中，则并没有创建新的列表对象
"""
li = [1, 2, 3]
print("id(li):", id(li))
li += [4]
print("li:", li)
print("id(li):", id(li))

# 原理解析
"""
Python 中的六个标准数据类型实际上分为两大类：可变数据和不可变数据。其中，
列表、字典和集合均为“可变对象”；而数字、字符串和元组均为“不可变对象”。
实际上上面演示的数值数据（即数字）和列表之间的差异正是这两种不同的数据类型导致的。
1,由于数字是不可变对象，我们不能够对数值本身进行任何可以改变数据值的操作
2,而作为可变对象，列表的值是可以在不新建对象的情况下进行改变的，因此对列表对象本身直接进行操作，
    是可以达到“改变变量值而不改变引用”的目的的。
"""
const_ref = 10000  #
const_ref1 = 10000
print(const_ref == 10000)  # True
print(const_ref1 is const_ref)  # False
# 即使是同样的数值，也可能具有不同的引用值。关键在于这个值是否来自于同一个对象。
print("id(const_ref):", id(const_ref))
print("id(10000):", id(10000))

# 除了getrefcount()函数的引用外，变量const_ref所引用的对象就只有1个引用也就是变量const_ref
# 一旦变量const_ref被释放，则相应的对象引用计数归零，也会被释放；并且只有此时，这个对象对应的内存空间才是真正的“被释放”。
const_ref1111 = 100001
print("getrefcount(const_ref1111):", getrefcount(const_ref1111))  # 2
print("getrefcount(10000) ", getrefcount(10000))  # 3

# 总结
"""
对于列表、字典和集合这些“可变对象”，通过对变量所引用对象本身进行操作，可以只改变变量的值而不改变变量的引用；
但对于数字、字符串和元组这些“不可变对象”，由于对象本身是不能够进行变值操作的，因此要想改变相应变量的值，就必须要新建对象，再把新建对象赋值给变量。
"""
