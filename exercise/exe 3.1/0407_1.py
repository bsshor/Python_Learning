# -*- encoding: utf-8 -*-
'''
@File : 0407_1.py
@Time : 2020/04/08 09:18:37
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    定义一个dog类(颜色, 名称), 里面有一个狗叫的方法; 
不同的狗叫声可能不一样;  然后实例化几条狗, 然后统计实例化狗的数量
'''

# here put the import lib


class dog(object):
    num = 0
    def __init__(self, color, name):
        self.color = color
        self.name = name
        dog.num += 1 #记录实例化dog的数量

    def bark(self):
        print("%s犬在叫"%(self.name))
    

dog1 = dog('金色', '拉布拉多')

dog1.bark()

dog2 = dog('黑色', '藏獒')

dog2.bark()

print("共有%d只犬"%(dog2.num))