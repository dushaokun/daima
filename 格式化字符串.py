# 格式化字符串
name = "张三"
age = 20
print("姓名" + name + ",年龄" + str(age) + "岁")
#这两个print输入的结果是一样的
print("姓名%s,年龄%d岁" %(name,age))

"""
在python字符串中如果有%，这个字符串就叫格式化字符串
%d 要格式化的是一个整数
%f 要格式化的是一个浮点数
%s 要格式化的是一个字符串
格式化字符串主要功能
把多个字符串及数字拼接到一块
"""
f = 3.14
str1 = "圆周率是："
print(str1+str(f))
print("%s%.2f" %(str1,f)) # #.2f 保留小数点后2位
a = 20
print("变量a的值为%05d" %a)  #保留5位，不够5位补零
#定义变量name
name = "小米"
print("我的名字叫%s，请多多关照" %name)

scale = 10.01
print("数据是%.2f %%" %scale)

company = input("请输入公司名称")
name = input("请输入姓名")
tel = input("请输入电话号码")
mailbox = input("请输入邮箱地址")
print("*"*20)
print("公司名称：%s" %company)
print("姓名：%s"%name)
print("电话：%s"%tel)
print("邮箱：%s"%mailbox)
print("*"*20)


