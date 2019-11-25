# 一,定义
"""
Python 中的字典提供了一种灵活的访问和组织数据的方式
字典是由很多值组成的集合
字典的索引可以是不同的数据类型，同样也不止是整数，也有字符串
字典的索引被称为“键”，键及键所关联的值叫键值对（类似于 Java 中的 Map 集合）
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
"""
dictionary = {'url1': 'baiDu', 'url2': 'google', 'num1': 12, 'num2': 34}


# 1,1字典的键
"""
键一般是唯一的，如果键重复，最后的一个键值对会替换前面的键值对，值没有唯一性要求，如下：
"""
dic1 = {'name': 'Mick', 'age': 23, 'address': 'BeiJing', 'name': 'jack'}
# 查看字典值发现重复的键值后面的替换前面的
# dic1 = {'name': 'jack', 'age': 23, 'address': 'BeiJing'}
print(dic1['name'])  # 'jack'


# 1.2字典的值
"""
#值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组，如下：
dict2 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258', ('a', 'b'): (12, 43)}
"""

# 1. 访问字典数据
"""
1,通过方括号里面添加键就可以直接进行访问
2,同样的，字典也可以用整数作为键，和列表的索引类似，只是字典的值是任何整数类型都行，
  不必要从0开始，因为键值的数据类型是任意的，
3,因为字典是不排序的，所以不能像列表那样切片。 如果访问字典中不存在的键，
  将导致 KeyError 出错信息。这很像列表的“越界” IndexError 出错信息。
"""
MyDog = {'size': 'big', 'color': 'white', 'character': 'gentle'}
# 字典值通过[‘键’]来访问
print("MyDog['size']", MyDog['size'])  # 输出结果:big
print('My Dog has ' + MyDog['color'] + ' fur.' + ' and it has a ' + MyDog['character'] + ' character')
# 输出结果 My Dog has white fur. and it has a gentle character

MyCon = {12: 'big', 0: 'white', 354: 'gentle', 1: 'good'}
# 访问键为 12 的字典值
print("MyCon[12]", MyCon[12])
# 访问键为 0 的字典值
print("MyCon[0]", MyCon[0])


# 2. 修改字典元素
"""
2.1 添加和更新字典数据
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
"""
dict3 = {'Name': 'Fiona', 'Age': 10, 'Class': 'Three'}
# 更新
dict3['Age'] = 8
# 添加
dict3['School'] = "Middle School"
# 查看字典数据
print("dict3", dict3)
# output:{'Name': 'Fiona', 'Age': 8, 'Class': 'Three', 'School': 'Middle School'}


"""
2.2 删除字典元素
对字典元素的删除操作能单一删除也能将整个字典清空，显示的删除一个字典使用 del 命令“
"""
dict4 = {'Name': 'Fiona', 'Age': 10, 'Class': 'Three'}
# 删除键是'Name'的条目
del dict4['Name']

# 清空字典所有条目
dict4.clear()

# 删除整个字典元素
del dict4

# print("dict4['Age']: ", dict4['Age'])  # 会报错
# print("dict4['School']: ", dict4['School'])  # 会报错


# 3. 字典的特性
"""
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住；
2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行；
"""

dict5 = {'Name': 'Fiona', 'Age': 10, 'Name': 'Manni'}
print("dict5['Name']: ", dict5['Name'])

# 以上实例输出结果：dict['Name']: Manni

# dict6 = {['Name']: 'Fiona', 'Age': 10}
# print("dict6['Name']: ", dict6['Name'])  # 报错


# 4,字典的函数
"""
4.1 len() 方法计算字典元素个数（键的总个数）
4.2 str() 方法输出字典中可以打印的字符串标识
4.3 type() 方法返回输入的变量类型，如果变量是字典就返回字典类型
"""
dict7 = {'Name': 'Fiona', 'Age': 10, 'class': 'Three'}
print("len(dict7)", len(dict7))
print("str(dict7)", str(dict7))
print("type(dict7)", type(dict7))


# 5,字典的方法
"""
5.1 dict.clear()删除字典内所有元素，clear() 方法没有任何返回值,实例如下：
"""
dict8 = {'Name': 'Fiona', 'Age': 10}
print("字典长度:%d" % len(dict8))
dict8.clear()
print("字典删除后长度 : %d" % len(dict8))

# 输出结果为：
# 字典长度 : 2
# 字典删除后长度 : 0


"""
5.2 dict.copy()方法对字典进行复制,这是深拷贝,# 浅拷贝: 引用对象,赋值dict2 = dict1 
"""
dict9 = {'Name': 'Runyon', 'Age': 7, 'Class': 'First'}
dict10 = dict9.copy()
print("dict10", dict10)
print("新复制的字典为 : ", dict10)

dict11 = {'user': 'Runyon', 'num': [1, 2, 3]}
# 浅拷贝: 引用对象  赋值
dict12 = dict11
# 拷贝
dict13 = dict11.copy()

# 修改 data 数据
dict11['user'] = 'root'
dict11['num'].remove(1)

# 输出结果
print("dict11", dict11)  # 会变化
print("dict12", dict12)  # 会变化
print("dict13", dict13)  # 不会变化


"""
5.3 dict.fromkeys() 创建一个新字典，以序列 seq 中元素做字典的键，val为字典所有键对应的初始值，该方法返回一个新的字典
fromkeys()方法语法：
dict.fromkeys(seq[, value])
# 参数
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
执行结果返回一个新的字典，如果不指定值默认为None,以上结果输出结果为：
"""
# dict.fromkeys(seq[, value])
seq = ('name', 'age', 'class')

# 不指定值
dict14 = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dict14))
# 新的字典为 : {'name': None, 'age': None, 'class': None}

# 赋值 10
dict15 = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dict15))
# 新的字典为 : {'name': 10, 'age': 10, 'class': 10}

# 　赋值一个元组
dict16 = dict.fromkeys(seq, ('zs', 8, 'Two'))
print("新的字典为 : %s" % str(dict16))
# 新的字典为 : {'name': ('zs', 8, 'Two'), 'age': ('zs', 8, 'Two'), 'class': ('zs', 8, 'Two')}


"""
5.4 dict.clear()删除字典内所有元素，clear() 方法没有任何返回值,实例如下：
get()方法语法:
        dict.get(key, default=None)
        # 参数
        key -- 字典中要查找的键。
        default -- 如果指定键的值不存在时，返回该默认值值。
"""
dict17 = {'Name': 'Mary', 'Age': 20}
print("Age 值为 : %s" % dict17.get('Age'))
print("Name 值为 : %s" % dict17.get('Name'))
print("Sex 值为 : %s" % dict17.get('Sex', "NA"))

# Age 值为 : 20
# Name 值为 : Mary
# Sex 值为 : NA


"""
5.5 key in dict 如果键在字典dict里返回true，否则返回false
"""
dict18 = {'Name': 'Mary', 'Age': 20, 'Address': 'BeiJing'}
# 检测键 Age 是否存在
if 'Age' in dict18:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

"""
5.6 dict.items()  item() 方法以列表返回可遍历的(键, 值) 元组数组
"""
dict19 = {'Name': 'Mary', 'Age': 17}
print("Value : %s" % dict19.items())
# 输出结果为：Value: dict_items([('Age', 17), ('Name', 'Mary')])

# 可遍历的元组数组举例：
dict20 = {'老大': '25岁',
          '老二': '20岁',
          '老三': '12岁',
          }
print(dict20.items())
for key, values in dict20.items():
    print(key + '已经' + values + '了')


"""
5.7 dict.keys() 返回一个迭代器，可以使用 list() 来转换为列表
"""
dict21 = {'Name': 'Mary', 'Age': 17}
print(dict21.keys())

# 以上结果输出为：dict_keys(['Name', 'Age'])
list1 = list(dict21.keys())
print("转换后的结果为 : %s" % list1)
# 输出结果为一个列表，后续可以对其进行相应操作：转换后的结果为: ['Name', 'Age']


"""
5.8 dict.values()
Python 字典 values() 方法返回一个迭代器，可以使用 list() 来转换为列表，
列表为字典中的所有值。
"""
dict22 = {'Name': 'Mary', 'Sex': 'male', 'Age': 7}
print("字典所有值为 : ", list(dict22.values()))
# 以上结果输出为：字典所有值为 :  ['Mary', 'male', 7]


"""
5.9 dict..setdefault(key, default=None)
Python 字典 setdefault() 方法和 get() 方法类似, 如果 key 在 字典中，
返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 
default ，default 默认值为 None。
setdefault()方法语法：
        dict.setdefault(key, default=None)
        # 参数
        key -- 查找的键值。
        default -- 键不存在时，设置的默认键值。
"""
dict23 = {'Name': 'Mary', 'Age': 17}

print("Age 键的值为 : %s" % dict23.setdefault('Age', None))
print("Sex 键的值为 : %s" % dict23.setdefault('Sex', None))
print("新字典为：", dict23)
# Age 键的值为 : 17
# Sex 键的值为 : None
# 新字典为： {'Age': 17, 'Name': 'Mary', 'Sex': None}


"""
5.10 dict..update(dict2) 
Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
语法：
    dict.update(dict2)
    # 参数
       dict2 -- 添加到指定字典dict里的字典，如果已存在更新
"""
dict24 = {'Name': 'Mary', 'Age': 17}
dictAdd1 = {'Sex': 'female'}
dictAdd2 = {'Age': '22'}

# 将 dict2 中的结果添加到字典 dict 中　
dict24.update(dictAdd1)
dict24.update(dictAdd2)
print("更新字典 dict : ", dict24)
# 更新字典 dict :  {'Name': 'Mary', 'Age': 17, 'Sex': 'female'}


"""
5.11 dict.pop(key[,default])
Python 字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。
key 值必须给出。 否则，返回 default 值。

pop()方法语法：
        pop(key[,default])
        #参数
            key: 要删除的键值
            default: 如果没有key，返回 default 值
        #返回值,
            返回被删除的值。
"""
dict25 = {'Name': 'Mary', 'Age': 17}
result = dict25.pop('Age')  # 删除
print(result)
# 以上结果输出为：
# 17
# Process finished with exit code 0


"""
5.12 dict.popitem()
Python 字典 popitem() 方法随机返回一个键值对(key,value)形式，按照 LIFO（ 
Last In First Out 后进先出法）顺序规则，即最末尾的键值对。 如果字典已经为空，
却调用了此方法，就报出KeyError异常。
"""

dict26 = {'Name': 'Mary', 'Age': 17}
pop_obj = dict26.popitem()
print(pop_obj)  # ('Age', 17)
print(dict26)  # {'Name': 'Mary'}

dict27 = {'Name': 'Mary', 'Age': 17}
# 将字典清空
del dict27
# print(dict27.popitem())  # 报错


"""
总结:
6、字典和列表
6.1 字典和列表差异:字典的无序性，列表的有序性
列表中的元素表项由于元素通过序列从0开始递增存放，所以列表中的表项是排序的，
而字典的内容的表项是不排序的，如下例子就很好的说明列表和字典的区别：

"""
list1 = ['zhangsan', 23, 'BeiJing']
list2 = ['BeiJing', 'zhangsan', 23]
print("list1 == list2",list1 == list2)  # False
dic28 = {'name': 'zhangsan', 'age': 23, 'address': 'BeiJing'}
dic29 = {'age': 23, 'name': 'zhangsan', 'address': 'BeiJing'}
print("list1 == list2",dic28 == dic29)  # True

# 由以上实例可以看出，当列表元素内容一致，顺序不同再对比内容时匹配不成功，
# 同理字典值匹配成功，说明字典中元素内容不按顺序存放。
