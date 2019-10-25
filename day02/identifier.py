# 第一行注释
print("hello python 第二个python")  # 单行注释
# 第二个注释
print("hello python 第三个python")
print("注释是解释代码的功能，")
"""
一对三个引号之间，这是多行注释
"""

# 类变量的定义
# 1,以单下划线开头 _foo 的代表不能直接访问的类属性，
# 需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
# 2,以双下划线开头的__foo代表类的私有成员，以双下划线开头和结尾的__foo__代表Python
# 里特殊方法专用的标识，如 __init__()代表类的构造函数。



#多行缩进,但是所有代码块语句必须包含相同的缩进空白数量

if True:
    print("neo")
else:
    print("smile")


# 多行语句
# Python 语句中一般以新行作为为语句的结束符。
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
# 语句中包含[], {} 或 () 括号就不需要使用多行连接符。如下实例：
item_one=1
item_two=2
item_three=3
total = item_one + \
        item_two + \
        item_three
print(total)

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']


class A:

    def __init__(self):
        pass

    def hello(self):
        pass


def main():
    pass