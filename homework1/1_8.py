"""
设计一个数据结构，用来存放10个员工的信息并初始化，
每个员工信息包括：工号，姓名，工龄，工资；  
将这10个员工，按照工资从高到低打印输出；
"""
# -*- encoding: utf-8 -*-
'''
@File : 1_8.py
@Time : 2020/03/04 23:01:02
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib

workers = {1: ('001', "晓萌", 3, 2332), 2: ('002', 'Bob', 1, 4000), 3: ('003', 'sdf', 11, 1000),
           4: ('004', 'ecob', 13, 14000), 5: ('005', 'dssdb', 4, 3000), 6: ('006', 'dcx', 7, 5000), 7: ('007', 'dcob', 1, 4500),
           8: ('008', 'dscx', 41, 110000), 9: ('009', 'cd32', 13, 14200), 10: ('010', 'ccvb', 6, 2000)}

i = 1
money = []
while i <= len(workers):
    money.append(workers[i][3])  # 将工资加入到列表
    i += 1
j = 0
money.sort()  # 对列表按从小到大排序
money.reverse()  # 逆序列表，实现从大到小排序
while j < len(workers):
    k = 1
    while k <= len(workers):

        if workers[k][3] == money[j]:
            print(workers[k])
            break
        k += 1
    j += 1
