"""
编写一个函数, 传入一个数字列表, 输出列表中的奇数;
数字列表请用随机数函数生成
"""


def output_odd(list):
    for i in list:
        if i % 2 == 1:
            print(i)
    return


li = [i for i in range(1, 45)]
output_odd(li)
