def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 3))
# 算术运算符
print(5 - 3)
print(5 + 3)
print(5 * 3)
print(6 / 3)  # 除
print(5 // 3)  # 取整除
print(5 % 3)  # 取余数
print(5 ** 3)  # 取幂
print("hello merit" * 3)  # 字符串与整数相乘，代表字符串重复整数次数
# 算数运算符的优先级顺序
print((3 + 2) * 5)
'''
**最高
* / // % 
+ -最低
'''
