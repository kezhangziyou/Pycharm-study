#
"""
import module1[, module2[,... moduleN]]
当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
调用的时候使用 模块名.函数名 来进行调用
"""
#  导入模块,调用sayhello函数
import hello
hello.sayHello()

# from … import …
"""
模块提供了类似名字空间的限制，允许 Python 从模块中导入指定的符号（变量、函数、类等）
到当前模块。导入后，这些符号就可以直接使用，而不需要前缀模块名。
"""
#  要导入模块 hello 的 sayhello 函数
from hello import sayHello
sayHello()



#from … import * 语句
"""
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

from modname import *
"""
from hello import *

sayHello()
world()
