# 取整数
from sqlalchemy import true

a = 9
b = 2
c = a // b
print(c)
# 求余数
left_num = 9
right_num = 2
result = left_num % right_num
print(result)
"""
1、数字与数字之间可以进行所以的运算
2、数字与字符串之间只能进行乘法运算
3、字符串和字符之间可以进行加法运算
"""
# 运算符字符串运算规则
mystr1 = 'hello'
mystr2 = 'world'
# 字符串只支持加法运算，拼接字符串
new_str = mystr1 + mystr2
print(new_str)
# 字符串与数字之间可以进行乘法运算，复制字符串
# 定义一个变量名name
name = "张三"
age = 26
print(name)
print(age)
# 超市买果
price = 8.5
weight = 10
money = price * weight
print(money)
# 买10斤减10块，变量定义之后，再=赋值，只是改变变量的值
money = money - 10
print(money)
# 两个变量，算数运算符计算
num_1 = 12
num_2 = 3
plus = num_1 + num_2
jian = num_1 - num_2
ji = num_2 * num_1
chu = num_1 / num_2
yu = num_1 % num_2
quzheng = num_1 // num_2

print(plus)
print(jian)
print(ji)
print(chu)
print(yu)
print(quzheng)
print(num_1 ** num_2)

# 变量值交换 m n
m = 10
n = 20
c = m
m = n
n = c
print(m, n)
# 显示python关键字
import keyword
print(keyword.kwlist)

# python的数据类型
'''
1.数字型
int (整型)
float(浮点型)
complex（复数型）
2. 布尔型
bool true 1 false 0
3. str 字符串
4. list 列表
5. tuple元祖
6. set  集合
7. dict 字典
8. None 不知道是哪种类型
'''
# 个人信息
name = '小明'
age = 18
gender = '男'
height = 1.75
isStudent = True
print(name, age, gender, height, isStudent)
# 变量赋值的时候，等号右边是什么数据类型，变量就是什么数据类型
i = 10
f = 10.5
h = True
print(i + f)
print(i - f)
print(i + h)
print(i - h)
# 数字型变量直接用算术运算符计算
# 布尔类型 true 代表 1 false 代表0


