#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : Main.py
@Time : 2020/6/24 23:25:58 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
程序入口模块
"""
import spider
import ava
def Basic_Message():
    """
    显示个人基本信息
    :return:
    """
    print('-*-' * 36)
    print("任务：1.爬取51job.com里“Python爬虫开发工程师”的薪资；2.计算北京地区该该岗位的平均工资")
    print("作者：邵博深")
    print("班级：软件1802")
    print("学号：120181080701")
    print('-*-' * 36)

if __name__ == '__main__':
    Basic_Message()
    print("数据原已爬取完毕，请问您是要重新爬取吗？")
    choice = input("请输入您的选择(y/n)：")

    if choice == 'y':
        print("努力爬取中ing(●'◡'●)")
        spider.Spider_51job()
        print("爬取完毕，下面开始计算北京地区的平均工资(∩_∩)")
        ava.Ava_Salary()
    elif choice == 'n':
        ava.Ava_Salary()

    else:
        exit(0)

