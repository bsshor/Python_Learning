"""
 编写一个函数cacluate,
 可以实现2个数的运算(加,减 乘,除)
"""


def cacluate(a, b):
    print("a+b=", a + b)
    print("a-b=", a - b)
    print("a*b=", a * b)
    print("a/b=", a / b)


print("请输入两个整数：")
a = int(input())
b = int(input())
cacluate(a, b)
