#  import 包名.包名.模块名
import cal.calculator


print("测试包的使用")

print(cal.calculator.add(1, 2))

# 但是导入调用的时候包名比较长，这样就可以使用from ... import ...语句来简化一下。
from cal import calculator

# 使用包的模块的方法
print(calculator.multiply(3, 6))
