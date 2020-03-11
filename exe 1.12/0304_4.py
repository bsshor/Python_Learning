"""
 创建一个有10个数字的列表,
 先输出此列表,
 然后再输出其中为偶数元素
"""
import random

num = [random.randint(1, 12123) for x in range(10)]  # 列表解析式，批量生成随机数
print(num)
for i in num:
    if i % 2 == 0:
        print(i)
