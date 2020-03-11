"""
    定义一个函数,来计算苹果的价格(重量*价格);
    通过键盘输入重量和价格,然后调用函数来计算
"""


def sum(a, b):
    return a * b


a = int(input("重量："))
b = int(input("价格："))

print("总价格:", sum(a, b))
