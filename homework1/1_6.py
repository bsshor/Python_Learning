"""
输出100以内的斐波那契数列
"""
# -*- encoding: utf-8 -*-
'''
@File : 1_6.py
@Time : 2020/03/04 21:29:49
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib

fibonacci = [1, 1]
while fibonacci[-1] < 100:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
if fibonacci[-1] >= 100:  # 如果最后一个元素大于100，则删除
    del fibonacci[-1]
for i in fibonacci:
    print(i)



