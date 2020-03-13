"""
将我们作业当中,  10个同同学成绩排序的问题,用 sort函数来实现;
这个10个同学的成绩,用列表存放, 列表里面每个元素是一个元组;
"""
import random

score = [random.randint(0, 100) for x in range(10)]
print(score)
dit1 = {}
for i in range(len(score)):
    dit1[i] = score[i]

print(dit1)
# sorted()，按值的大小对键排序
dot2 = sorted(dit1.items(), key=lambda item: item[1], reverse=True)
for key, value in dot2:
    print(key, ":", value)
