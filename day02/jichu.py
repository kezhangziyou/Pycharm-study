# 1-数学计算
print(10 + 20);  # 加
print(10 - 20);  # 减
print(10 * 20);  # 乘
print(10 / 20);  # 除
print(9 // 2);  # 取整数
print(9 % 2);  # 取余
print(9 ** 2);  # 幂次方
message="对不起" * 5;
print(message);
print((2+3)*5);  # 括号
# 2-变量定义

qq_number="392506068";
qq_password="123";
print(qq_number);

""""
2变量定义，两个值相乘
qq_number="392506068";
qq_password="123";
print(qq_number);
"""

# 单价
price = 8.5;
# 重量
weight = 7.5;
# 总价
money = weight * price;
# 返还5块钱。
money = money - 5;
print(money);
# 3定义变量时不需要指定变量的类型
name1="小明";
age=18;
sex=True; #布尔型
sex1=False;
# 3类型：整形，浮点型，布尔型，复数型，字符串，列表，元素，字典，type()查看变量的类型
print(type(name1));
# 字符串的拼接，直接用+号
first_name="Zhang";
last_name="Ke";
name=first_name+last_name;
print(name);
# 4变量的输入input(x)，返回的是 字符串类型,type(x);
# 5类型转换函数，int(x)将x转换为一个整数
# 1.输入苹果额单价
price_str=input("苹果的单价");
# 2。输入苹果的重量
weight_str=input("苹果的重量")
# 3。总金额
money=float(price_str)*float(weight_str);
print(money)

"""
变量的输入
1变量的输入input(x)：返回的是字符串类型,
2type(x)得到x的类型;
3类型转换函数，int(x)将x转换为一个整数

"""
#
# 1.输入苹果额单价
price=float(input("苹果的单价"));
# 2。输入苹果的重量
weight=float(input("苹果的重量"));
# 3。总金额
money=price*weight;
print(money);
#变量的格式化输出%s字符串,%d整数,%f小数,%%百分号
name="小明";

print(" 我的名字叫%s请多多关照!" %name);
#print(" "格式化字符串"%变量1");


"""
格式化输入
"""
#变量的格式化输出%s字符串,%d整数,%f小数,%%百分号
name="小明";

print(" 我的名字叫%s请多多关照!" %name);
student_no=1;
print(" 我的学号是%06d" %student_no);# %06d显示六位整数，不足补0
price=8.5;
weight=7.5;
money=price*weight;
print("苹果的单价是%.2f元/斤，购买了%.2f斤，支付%.2f元" %(price,weight,money));
scale=0.25;
print("数据比例是%.2f%%"% scale*10); #字符串复制了10遍输出的
print("数据比例是%.2f%%"%(scale*10)); #数字乘以10倍输出。
print("数据比例是%f%%"%scale); #默认输出6位小数。
# 标识符，字母、下划线、数字，不能是数字开头，
import keyword; #导入关键字包
print(keyword.kwlist);


"""
条件判断
"""
age=18

if age>=18:
    print("成年，可以进网吧")

