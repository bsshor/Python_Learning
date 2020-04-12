#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : Student.py
@Time : 2020/4/11 00:55:27 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
Python学生成绩管理系统
"""

import pymysql
import os

class StudentScore(object):
    def __init__(self):
        self.Name = None
        self.Id = None
        self.Class = None
        self.Score = None

        # 连接数据库
        self.db = None

        # 使用cursor()方法获取操作游标
        self.cursor = None

    def append(self):
        """
        增
        :return:
        """
        Name = input("请输入学生姓名：")
        Id = input("请输入学生学号：")
        Class = input("请输入学生班级：")
        Score = input("请输入学生Python成绩：")

        sql = 'INSERT INTO `my_test`.`pyhton_score` (`班级`, `学号`, `姓名`, `Python成绩`) VALUES (%s, %s, %s, %s)' % (
            Class, Id, Name, Score)

        try:
            self.cursor.execute(sql)  # 执行sql语句
            self.db.commit()  # 提交到数据库执行
        except Exception as e:
            print(e)

        print("新增成功")

    def delete(self):
        """
        删
        :return:
        """
        Id = input("请输入要被删除学生的学号：")
        sql = 'DELETE FROM `my_test`.`pyhton_score` WHERE (`学号` = %s)' % (Id)

        try:
            self.cursor.execute(sql)  # 执行SQL语句
            self.db.commit()  # 提交修改
        except Exception as e:
            print(e)
        print("删除成功")

    def updata(self):
        """
        改
        :return:
        """
        Id = input("请输入待更新成绩学生的学号：")
        Score = input("请输入这位同学的成绩：")
        sql = 'UPDATE `my_test`.`pyhton_score` SET `Python成绩` = %s WHERE (`学号` = %s)' % (Score, Id)

        try:
            self.cursor.execute(sql)  # 执行SQL语句
            self.db.commit()  # 提交修改
        except Exception as e:
            print(e)
        print("修改成功")

    def search(self):
        """
        查
        """
        Id = input("请输入待查询成绩学生的学号：")
        sql = "SELECT * FROM `my_test`.`pyhton_score`  WHERE 学号 = %s" % (Id)
        try:
            self.cursor.execute(sql)  # 执行SQL语句
            results = self.cursor.fetchall()  # 获取所有记录列表
            # print(results)

            if results:
                # 打印结果

                print(">>>查询结果\n班级：%s\n学号：%s\n姓名：%s\nPyhton成绩：%s" % (results[0][0], results[0][1], results[0][2], results[0][3]))
            else:
                print("查无此人")
        except Exception as e:
            print("e:", e)

    def searchall(self):
        """
        查询所有学生信息
        :return:
        """

        sql = "SELECT * FROM pyhton_score"
        try:

            self.cursor.execute(sql)  # 执行SQL语句
            results = self.cursor.fetchall()  # 获取所有记录列表
            print("%s           %s        %s    %s" % ("班级", "学号", "姓名", "Python成绩"))
            for row in results:
                Class = row[0]
                Id = row[1]
                Name = row[2]
                Score = row[3]
                # 打印结果
                print("%s    %s    %3s    %s" % (Class, Id, Name, Score))
        except Exception as e:
            print(e)

    def menu(self):
        """
        功能菜单
        :return:
        """
        # 此处密码保密，文件夹里有导出的csv数据，可以适配到本地数据库
        self.db = pymysql.connect("localhost", "root", "************", "my_test", charset='utf8')

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

        # 功能选项
        # option = {0: 'searchall()', 1: 'search()', 2: 'delete()', 3: 'append()', 4: 'updata()'}

        excute = True

        while excute:

            print(">>>>>>>菜单:")
            print("0： 查询所有学生成绩信息")
            print("1： 查询指定学生信息")
            print("2： 删除指定学生信息")
            print("3： 添加新学生信息")
            print("4： 更改学生成绩信息")
            print("5： 退出系统")

            choice = int(input("请输入您想要执行操作的序号："))
            if choice == 5:
                print("您已退出系统，期待您的下次使用")
                break
            else:
                while True:
                    if choice == 0:
                        self.searchall()
                    elif choice == 1:
                        self.search()
                    elif choice == 2:
                        self.delete()
                    elif choice == 3:
                        self.append()
                    elif choice == 4:
                        self.updata()
                    flag = input("您还要继续当前操作吗(y or n):")
                    if flag == 'y':
                        continue
                    else:
                        break
        # 关闭数据库连接
        self.db.close()


if __name__ == "__main__":
    admin = StudentScore()  # 实例化对象——管理员
    print("--------------->>欢迎访问Pyhton成绩管理系统！<<---------------")
    admin.menu()
