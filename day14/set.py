"""
Python 也包含有 集合 类型。集合是由不重复元素组成的无序的集。它的基本用法包括成员检测和消除重复元素。
集合对象也支持像 联合，交集，差集，对称差分等数学运算。
"""
set1 = {'hello', 'hello', 'word', 'word'}
print(set1)
# 　输出结果实现自动去重{'hello', 'word'}

# 1、集合创建
"""
可以使用大括号 { } 或者 set() 函数创建集合，
创建格式：
param = {value01,value02,...}
或者
set(value)
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
# 创建空集合
empty_set = set()
print(":", )
print("type(empty_set) :", type(empty_set))  # <class 'set'

# 创建空字典
empty_dict = {}
print("type(empty_dict):", type(empty_dict))  # <class'dict'


# 2、集合的基本操作
# 2.1 添加元素
"""
语法格式：
1,s.add(x):将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
2,s.update( x ):也可以添加元素，并且参数可以是列表，元组，字典等，语法格式如下：
    参数 x 可以是一个，也可以是多个，多个参数之间用逗号相隔
"""

s1 = set(('hello', 'world'))
print("s1:", s1)

# 向集合 s 中添加元素
s1.add('!')
print('添加元素!后的集合是：%s' % s1)  # {'world', '!', 'hello'}

# 1）添加列表
s1.update([1, 3], [2, 4])
print('添加元素[1, 3], [2, 4]后的集合是：%s' % s1)

# 2）添加元组
s1.update(('h', 'j'))
print("添加元素('h', 'j')后的集合是：%s" % s1)


# 2.2 移除元素
"""
语法格式如下：
s.remove( x ) :将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
s.discard( x ):移除集合中的元素，且如果元素不存在，不会发生错误.
s.pop(): 随机删除集合中的一个元素

"""

# 将元素 2 从集合中移除
s2 = set(('hello', 'world'))
s2.remove('hello')
print('移除元素hello后的集合是：%s' % s2)

# 如果移除集合中不存在的元素会报异常
# s2.remove('hi') # 移除集合中不存在的集合,报错
print('移除元素后的集合是：%s' % s2)

s3 = set(("Google", "Runoob", "Taobao"))
s3.discard("Facebook")  # 不存在不会发生错误
print("set3:", s3)
print(":", )

# 随机删除集合中的一个元素
s3.pop()

print('移除元素后的集合是：%s' % s3)

# 2.3 计算集合元素个数
"""
语法格式如下：
len(s):计算集合 s 元素个数。
"""

s4 = {1, 3, 4, 'world', '!', 'hello', 'h', 'j'}
print('集合 s 的长度是：%s' % len(s4))  # 输出结果 集合 s4 的长度是：8

# 2.4 清空集合
"""
语法格式如下：s.clear()清空集合 s
"""
s5 = {1, 3, 4, 'world', '!', 'hello', 'h', 'j'}

s5.clear()
print('集合清空后的结果是：%s' % s5)  # 输出结果：集合清空后的结果是：set()

# 2.5 判断元素是否存在
"""
语法格式如下： x in s,判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。
"""
# 判断元素是否存在
s = {'hello', 'word'}
# 判断元素 hello 是否在集合 s 中

print('hello' in s)  # 输出结果：True

# 2.6 集合运算
"""
集合之间的运算符分别是‘-’、‘|’、‘&’、‘^’ ; 下面以两个集合之间的运算为例进行讲解：

‘-’：代表前者中包含后者中不包含的元素
‘|’：代表两者中全部元素聚在一起去重后的结果
‘&’：两者中都包含的元素
‘^’：不同时包含于两个集合中的元素
"""
a = set('afqwbracadaagfgbrafg')
b = set('rfgfgfalacazamddg')
print("a:", a)
print("b:", b)

print("集合a中包含而集合b中不包含的元素,a - b:", a - b)  # {'b', 'w', 'q'}
print("集合a或b中包含的所有元素,a | b:", a | b)  # {'d', 'g', 'l', 'c', 'r', 'q', 'b', 'w', 'f', 'z', 'm', 'a'}
print("集合a和b中都包含了的元素,a & b:", a & b)  # {'r', 'd', 'g', 'f', 'c', 'a'}
print("不同时包含于a和b的元素a ^ b:", a ^ b)  # {'l', 'q', 'b', 'w', 'z', 'm'}

# 3、集合推导式
"""
和列表一样，集合也支持推导式

"""

# 判断元素是否存在
a = {x for x in 'abracadabra' if x not in 'abc'}
# a{'r', 'd'}


# 4、集合内置方法
# 4.1 difference()
"""
difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，
但不包含在第二个集合(方法的参数)中，返回一个新的集合。 
set.difference(set)
"""

# 求两个集合的差集，元素在 x 中不在 y 中
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print('两个集合的差集是：%s' % z)  # 输出结果为：{'cherry', 'banana'}


# 4.2 difference_update()
"""
difference_update() 方法用于移除两个集合中都存在的元素。
difference_update() 方法与 difference() 方法的区别在于difference() 方法返回一个移除相同元素的新集合，而 
difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)  # 结果为：{'banana', 'cherry'}

x1 = {1, 2, 3, 4}
y1 = {1, 2, 3}
x1.difference_update(y1)
print(x1)  # 结果为：{4}


# 4.3 intersection()
"""
intersection() 方法用于返回两个或更多集合中都包含的元素，即交集，返回一个新的集合。
intersection() 方法语法：
    set.intersection(set1, set2 ... etc)
        参数：
            set1 -- 必需，要查找相同元素的集合
            set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
"""

# 返回两个或者多个集合的交集
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.intersection(y)
print("z:", z)

# 　返回三个集合的交集
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print('三个集合的差集是：%s' % result)
# 输出结果：{'apple'}
# 两个集合的差集是：{'c'}

# 4.4 intersection_update()
"""
intersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。
intersection_update() 方法不同于 intersection() 方法，因为 intersection() 
方法是返回一个新的集合，而 intersection_update() 方法是在原始的集合上移除不重叠的元素。
set.intersection_update(set1, set2 ... etc)
    参数
        set1 -- 必需，要查找相同元素的集合
        set2 -- 可选，其他要查找相同元素的集合，可以使用多个多个，多个使用逗号‘,’ 隔开
"""
# 返回一个无返回值的集合交集
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

x.intersection_update(y)
print(x)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)

print(x)

# 　输出结果：
{'apple'}
{'c'}

# 4.5 union()
"""
union();方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次，返回值返回一个新的集合
语法：
    set.union(set1, set2...)
    参数
        set1 - - 必需，合并的目标集合
        set2 - - 可选，其他要合并的集合，可以多个，多个使用逗号, 隔开。
"""

# 合并两个集合，重复元素只会出现一次：

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.union(y)
print(z)
# 输出结果为：{'cherry', 'runoob', 'google', 'banana', 'apple'}

# 合并多个集合：
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)  # 输出结果为：{'c', 'd', 'f', 'e', 'b', 'a'}
# 4.6 isdisjoint()
"""
isdisjoint()方法用于判断两个集合是否包含相同的元素， == 如果没有返回
True，否则返回False。 ==
方法语法：set.isdisjoint(set)
"""

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
# 　判断集合 y 中是否包含集合 x 中的元素，如果没有返回 True, 有则返回 False
z = x.isdisjoint(y)
# 结果返回 False,说明集合 y 中有和 x 中相同的元素
print(z)  # False

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "baidu"}
# 　判断集合 y 中是否包含集合 x 中的元素，如果没有返回 True, 有则返回 False
z = x.isdisjoint(y)
# 结果返回 True,说明集合 y 中没有和 x 中相同的元素
print(z)  # True

# 4.7issubset()
"""
issubset()方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回
True，否则返回False。
语法:
set.issubset(set)
    参数 
        set - - 必需，要比查找的集合返回值返回布尔值，如果都包含返回True，否则返回False。
"""
# 判断集合 x 的所有元素是否都包含在集合 y 中：
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

# 输出结果
# # 说明 集合 x 中的元素都包含在 y 中
# True
# 注意： 必须是集合中的元素都包含在内，否则结果为
# False

# 　集合 y 中只有元素 b 和 c ，执行结果为 False
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "y"}

z = x.issubset(y)

print(z)  # 结果输出；False
# 4.8 issuperset()
"""
issuperset()
方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回True，否则返回False。
语法：set.issuperset(set)
"""
# 判断集合 y 的所有元素是否都包含在集合 x 中：
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)

print(z)  # 输出结果为： True

# 如果没有全部包含返回 False：


x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)  # 输出结果为：False
# 4.9 symmetric_difference()
"""
symmetric_difference()
方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素，结果返回一个新的集合。
语法：
set.symmetric_difference(set)
"""

# 返回两个集合组成的新集合，但会移除两个集合的重复元素：
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.symmetric_difference(y)

print(z)  # 输出结果：{'banana', 'google', 'cherry', 'runoob'}
# 4.10 symmetric_difference_update()
"""
symmetric_difference_update()
方法移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。

语法：set.symmetric_difference_update(set)
"""

# 在原始集合 x 中移除与 y 集合中的重复元素，并将不重复的元素插入到集合 x 中：
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

x.symmetric_difference_update(y)

print(x)

# 输出结果：{'runoob', 'cherry', 'banana', 'google'}
