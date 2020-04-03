"""
编写一个函数,接收n个数字，求这些参数数字的和
"""


def sum(n):
    sum = 0
    for i in range(n):
        sum += float(input())
    print("sum = ", sum)


sum(int(input("请问您要输入几个数字：")))
