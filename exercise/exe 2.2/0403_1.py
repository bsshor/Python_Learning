# -*- encoding: utf-8 -*-
'''
@File : 0403_1.py
@Time : 2020/04/03 08:40:22
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''
"""
利用闭包返回一个计数器函数，每次调用它返回递增整数
定义createCounter()

"""
# here put the import lib
def createCounter():
    
    i = [0]

    def counter():
        i[0] += 1
        return i[0]
    return counter
    
    return counter

# 测试:

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')