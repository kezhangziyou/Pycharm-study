# 列表
"""
列表俗称是 Python 中的苦力，列表可变（可以改变列表的内容）
列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
"""
#  创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

# 1-列表函数
"""
1.1 list 函数
1.2 len 函数
1.3 max 函数
1.4 min 函数
"""
list1 = ['baidu', 'google', 12, 34];
list2 = [1, 2, 3, 4, 5];
list3 = ["a", "b", "c", "d"];
ll = list('hello')
print(ll)  # ['h', 'e', 'l', 'l', 'o']
print("ll[2]:", ll[2])
ll[2] = '5'
print("修改后的ll:", ll)
print("len(ll):", len(ll))
list_num = [2, 3, 5, 6, 8, 12]
print("max(list_num):", max(list_num))
print("min(list_num):", min(list_num))

# 2 列表方法
"""
2.1 append 方法用于在列表的末尾追加新的内容,入栈
2.2 count  方法用于统计某个元素在列表中出现的次数
2.3 extend 方法表示追加内容，它可以在列表的末尾一次性追加另一个序列中的多个值，也就是用新列表扩展原有列表
2.4 index 方法用于从列表中找出某个元素第一次匹配的位置的索引位置
2.5 insert  方法用于像列表中插入对象
2.6 pop  方法会移除列表中的一个元素（默认是最后一个），并且返回该元素的值,出栈
2.7 remove 方法用于移除列表中第一个匹配的元素
2.8 reverse  方法是将列表中的元素进行反转操作
2.9 sort 方法用于在原位置排序，‘原位置排序’意味着改变原来的列表而让列表中的元素有顺序排列
2.10 clear 方法用于清空列表
2.11 copy
copy 方法是复制列表
"""
list_append = [1, 2, 3, 4, 5]
print("list_append:", list_append)

num = [1, 2, 3, 4, 5, 5, 5, 5, 6]
# 统计num列表中5出现的次数
print("num.count(5):", num.count(5))

a = [1, 2, 3]
b = [4, 5, 6]
# 将列表b追加在列表a后面
a.extend(b)
print("a:", a)

# 连接操作不改变原有列表
a = [1, 2, 3]
b = [4, 5, 6]
print("a + b:", a + b)

content = ['where', 'who', 'lisi', 'cntent', 'who']
print("content.index('who'):", content.index('who'))

num = [1, 2, 5, 6, 7]
num.insert(2, 3)
print("num:", num)

x = [1, 2, 3]
x.pop()
print("x:", x)
x.append(x.pop())
print("x.append(x.pop())不会变:",x )

content = ['where', 'who', 'lisi', 'cntent', 'who', 'who']
content.remove('who')
# 移除了第一个匹配的元素
print("content.remove('who'):",content )

x = [2, 3, 5, 6, 1, 4, 7]
x.reverse()
print("x.reverse():", x)
x.sort()
print("x.sort():", x)
x.clear()
print("x.clear():", x)

list1 = ['baidu', 'google', 12, 23]
list2 = list1.copy()
print("list2:", list2)



# 3 列表基本操作
"""
列表可以使用所有适用于序列的标准操作，比如第7天所学的索引、分片、连接和相乘，
更有趣的是，列表是可以修改的，也就是定义的列表内容可以根据需求更改，本节介绍
一些改变列表的方法：如元素赋值、元素删除、分片赋值以及列表方法（但是请注意，
并不是所有的列表方法都能真正改变列表）
"""
# 3.1 改变列表：元素赋值
# 在列表中要给指定的元素赋值时，我们需要指定特定的索引标记来为列表中某个特定的，位置明确的元素赋值，比如 x[3]=5


#
x=[1,2,3,4,5]
print("改变前:",x)
# 改变列表第四个元素的内容
x[3]=5
print("改变后:",x)


#3.2 删除列表元素
# 若要删除列表中的元素，直接利用del删除即可

# 定义长度为4的姓名列表
names=['zhangsan','lisi','wangwu','zhaoliu']
print("改变前:",names)

# 删除第三个元素
del names[2]
# 最后列表长度由4变为3
print("改变前:",names)


# 3.3 分片赋值
# 在 Python 中对序列或者列表的分片操作是一个很强大的特性，分片赋值会显得更加强大，例如：

# 3.3.1定义一个list
name = list('Pyther')

# 改变 list 中的最后两个值
name[4:]='on'
print("改变前:",name) # ['P', 'y', 't', 'h', 'o', 'n']

# 从上可知，程序可以一次为多个元素赋值，在分片赋值时，可以使用与原序列不等长的序列将分片替换，例如：
name_re = list('perl')
name_re
['p', 'e', 'r', 'l']

# 3.3.2分片替换
name_re[1:] = list('ython')
print("name_re:",name_re) # ['p', 'y', 't', 'h', 'o', 'n']


# 分片赋值还可以在不需要更改原有列表任何内容的情况下进行新元素插入
num = [1,4,5]
# 在第一个元素后插入新的元素
num[1:1]=[2,3]
name_re = list('perl')
print("name_re:",name_re)  #[1, 2, 3, 4, 5]

# 3.3.3同理也可以通过分片操作来删除列表中的元素，同样也支持负数分片操作

num
[1, 2, 3, 4, 5]

# 给第一个和第三个元素之间分片赋值一个空序列，即删除元素
num[1:3] = []


# 负数分片操作
num[-1:-1] = [5,5,5]
print("num:",num) # [1, 2, 3, 4, 5, 5, 5, 5]





















