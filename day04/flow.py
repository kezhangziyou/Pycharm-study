# if语句
"""
if 判断条件：
    执行语句……
else：
    执行语句……
关键字 ‘elif’ 是 ’else if’ 的缩写
"""
x = int(input("Please enter an integer: "))
x = -5
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for 循环
"""
Python for 循环可以遍历任何序列的项目，如一个 列表 或者一个 字符串。
'''
for 后跟变量名，in 后跟序列，注意加冒号
for 循环每次从序列中取一个值放到变量中
此处的序列主要指 列表  元组   字符串   文件
'''
for iterating_var in sequence:
   statements(s)
"""
print('-------对象循环:----------')
for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前字母 :', fruit)

# 也可以通过索引地址来遍历内容
print('-------地址循环:----------')
sting = 'Python'
for index in range(len(sting)):  # 第一个实例
    print('当前字母 :', sting[index])

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])

# while 循环
"""
while 判断条件：
    执行语句……
"""
print('-------while循环:----------')
count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1
print('-------while+else循环:----------')
count1 = 0
while count1 < 7:
    print(count1, " is  less than 6")
    count1 = count1 + 1
else:
    print(count1, " is not less than 6")

# range()函数
print('-------range()函数:----------')
"""
如果你需要一个数值序列，内置函数 range() 会很方便，它生成一个等差级数链表:
range (start， end， scan):
参数含义：
    start:计数从 start 开始。默认是从 0 开始。例如 range(5) 等价于 range(0, 5);
    end:  计数到 end 结束，但不包括 end.例如：range(0, 5) 是[0, 1, 2, 3, 4]没有 5
    scan：每次跳跃的间距，默认为1。例如：range(0, 5) 等价于 range(0, 5, 1)
"""
for i in range(6):
    print(i)
print(range(6), 'finish')

for i in range(6, 10):
    print(i)
print(range(6, 10), 'finish')

for i in range(6, 12, 2):
    print(i)
print(range(6, 12, 2), 'finish')
# 需要迭代链表索引的话，如下所示结合使 用 range() 和 len():
a = ['i', 'love', 'coding', 'and', 'free']
for i in range(len(a)):
    print(i, a[i])

# break用法
print('-------break用法:----------')
"""
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，
任何对应的循环 else 块将不执行。
"""
for letter in 'ityouknow':  # 第一个实例
    if letter == 'n':  # 字母为n时中断
        break
    print('当前字母 :', letter)

# continue用法
print('-------continue用法:----------')
"""
continue 语句被用来跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
"""
for letter in 'ityouknow':  # 第一个实例
    if letter == 'n':  # 字母为 n 时跳过输出
        continue
    print('当前字母 :', letter)

# pass语句
print('-------pass语句:----------')
"""
Python pass 是空语句，是为了保持程序结构的完整性。它用于那些语法上必须要有什么语句，
但程序什么也不做的场合.
"""
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# 这通常用于创建最小结构的类:

class MyEmptyClass:
    pass



