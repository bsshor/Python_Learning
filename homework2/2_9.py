"""
 定义一个函数，函数接收一个数组，
 并把数组里面的数据从小到大排序(冒泡排序, 也可以直接使用相关的函数)
"""
import random


def array(li=[]):
    print(sorted(li))


# 列表解析式生成随机批量生成
arrays = [random.randint(0, 1000) for i in range(1, 21)]

array(arrays)
