# 一,类的定义
class Car:
    # 定义类中的属性
    name = 'BMW'
    pass


# 创建 Car 的实例对象 c
c = Car()

# 二,类中的方法
"""
2.1 内置方法
方法	说明
__init__	构造函数，在生成对象时调用
__del__	析构函数，释放对象时使用
__repr__	打印，转换
__setitem__	按照索引赋值
__getitem__	按照索引获取值
__len__	获得长度
__cmp__	比较运算
__call__	函数调用
__add__	加运算
__sub__	减运算
__mul__	乘运算
__div__	除运算
__mod__	求余运算
__pow__	乘方
2.2 自定义方法
Python 有三种常见的方法，分别为：实例方法、类方法、静态方法，这三种方法都定义在类中。
"""

'''
3.2.1 类方法
类方法是将类本身作为对象进行操作的方法。
类方法（可调类变量、可被实例调用、可被类调用）
1、类方法通过@classmethod装饰器实现，只能访问类变量，不能访问实例变量；
2、通过cls参数传递当前类对象，不需要实例化。
'''


class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    @classmethod
    def run(cls, speed):
        print(cls.name, speed, '行驶')


# 访问方式1
c = Car("宝马")
c.run("100迈")
# 访问方式2
Car.run("100迈")

# 2.2.2静态方法

'''
静态方法是类中的函数，不需要实例。
定义与使用
静态方法（可调类变量、可被实例调用、可被类调用）
1、用 @staticmethod 装饰的不带 self 参数的方法；
2、静态方法名义上归类管理，实际中在静态方法中无法访问类和实例中的任何属性；
3、调用时并不需要传递类或实例。
'''


class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def run(speed):
        print(Car.name, speed, '行驶')


# 访问方式1
c = Car("宝马")
c.run("100迈")
# 访问方式2
Car.run("100迈")

# 3.2.3 实例方法
'''
实例方法就是类的实例能够使用的方法。
定义与使用
实例方法（可调类变量、可调实例变量、可被实例调用）
第一个参数强制为实例对象 self。
'''


class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    def run(self, speed):
        print(self.name, speed, '行驶')


# 访问
c = Car("宝马")
c.run("100迈")

# 三,类的继承
'''
定义与使用
基本语法：class ClassName(BaseClassName)
'''


# 父类
class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    def run(self, speed):
        print(self.name, speed, '行驶')


# 子类
class BMWCar(Car):
    conf = "经济适用型"
    pass


# 调用父类 Car 中 run 方法
bc = BMWCar("BMW经济适用型轿车")
bc.run("100迈")


# 四,类的多态
'''
定义与使用
'''


# 父类
class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    def run(self, speed):
        print('Car-->', self.name, speed, '行驶')


# 子类1
class BMWCar(Car):
    def run(self, speed):
        print('BMWCar-->', self.name, speed, '行驶')


# 子类2
class SVWCar(Car):
    def run(self, speed):
        print('SVWCar-->', self.name, speed, '行驶')


# 调用 run 方法
c = Car("Car")
c.run("120迈")

bc = BMWCar("宝马")
bc.run("100迈")

sc = SVWCar("大众")
sc.run("80迈")

# 输出结果
'''
Car--> Car 120迈 行驶
BMWCar--> 宝马 100迈 行驶
SVWCar--> 大众 80迈 行驶
在上面的例子中，我们可以看出：c、bc 、sc是不同类型的对象，在它们调用run方法时，调用的均是各自类中的方法，这就是多态。
'''
