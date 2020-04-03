"""
元素输出和查找：  
请输出0-50之间的奇数，偶数，质数,能同时被2和3整除的数
"""
# -*- encoding: utf-8 -*-
'''
@File : 1_1.py
@Time : 2020/03/04 22:08:41
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib
num = list(range(0,51))

#输出奇数
print('0-50之间的偶数为：')
for i in num:
    if i%2==1:
        print(i, end=' ')
print()

#输出偶数
print('0-50之间的奇数为：')
for i in num:
    if i%2==0:
        print(i, end=' ')
print()

#输出质数
print("0-50之间的质数为：")

for i in num[2:-1] :
    # if i == 1 or i ==0:
    #     break
    # elif i == 2:
    #     print('2', end=' ')
    # elif i>2:
    flag = True
    for  x in range(2,i):
        if i % x == 0:
            flag = False
            break
    if flag:
        print(i, end=' ')

print("\n")




#同时能被2和3整除的数
print("同时能被2和3整除的数为：" )
for i in num:
    if i % 2 == 0 and i % 3 == 0:
        print(i,end =" ")
