#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : ava.py
@Time : 2020/6/21 16:11:14 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：

"""
import Model.model as model


def Ava_Salary():
    datas = model.Jobs.search_all()
    i = 1
    min = []
    max = []

    for salary in datas:
        # print(i, salary[0])
        i += 1
        if salary[0][-3:] == "万/月":

            salary = salary[0].split('-')
            min.append(float(salary[0]))
            max.append(float(salary[1][0:-3]))
        else:
            salary = salary[0].split('-')
            min.append(float(salary[0]) * 0.1)
            max.append(float(salary[1][0:-3]) * 0.1)
    try:
        minava = sum(min) / len(min)
        maxava = sum(max) / len(max)
    except Exception as e:
        print(type(e), ':', e)




    print("平均月工资:", str(minava)[:5], '~', str(maxava)[:5], "万/元")


if __name__ == '__main__':
    # test
    Ava_Salary()
