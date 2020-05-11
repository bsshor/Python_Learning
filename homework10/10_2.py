#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 10_2.py
@Time : 2020/5/9 08:09:50 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
"""
import pymysql


class database():
    def __init__(self, host='localhost', user='root', passwd='root', db='', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def exit(self):

        self.cursor.close()
        self.conn.close()

    def create(self):
        """
        创建
        """
        cursor = self.cursor
        sql = """
CREATE TABLE for_study.message_pad (
  create table message_pad
(
    id         int auto_increment
        primary key,
    message    text                                null,
    author     varchar(45)                         null,
    time       timestamp default CURRENT_TIMESTAMP null,
    is_deleted int       default 0                 null
)
    comment '留言本';
        """
        # 主键采用自增模式

        cursor.execute(sql)

    def append(self):
        """
        增(插)
        """
        cursor = self.cursor
        conn = self.conn
        theme = input("请输入您要留言的内容:")
        name = input("请留下您的姓名:")
        # SQL 插入语句
        sql = """INSERT INTO for_study.message_pad (`message`, `author`)
        VALUES (\'%s\',\'%s\');""" % (theme, name)
        # print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
            print("留言成功!")
        except Exception as e:
            print(type(e), e)
            # 发生错误时回滚
            conn.rollback()

    def search(self, Id=None):
        """
        查
        """
        cursor = self.cursor

        # 只查询未被删除的信息
        if Id == None:
            sql = 'SELECT * FROM for_study.message_pad where is_deleted = 0;'
        else:
            sql = 'SELECT * FROM for_study.message_pad where id = %d and is_deleted = 0;' % Id

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            # print(type(results))
            # 查询结果为空时为 (),类型是元组
            # 不为空时为
            # [{'id': 15, 'message': '21史蒂芬森', 'author': '是吧撒大莎', 'time': datetime.datetime(2020, 5, 11, 3, 9, 26), 'is_deleted': 0}]
            # 查询结果是一个列表,元素为由行组成的字典
            # 字典的键和值分别是每个列的列名和对应的内容
            if results == ():
                print("您所选的ID不存在或其记录已被删除!")
            else:
                for row in results:
                    Id = row['id']
                    message = row['message']
                    name = row['author']
                    time = row['time']
                    print('-' * 100)
                    print('ID:', Id, '  time:', time)
                    print('name:', name)
                    print("message:", message)
                    print('-' * 100)
        except Exception as e:
            print(type(e), ':', e)



    def update(self):
        """
        改
        """
        cursor = self.cursor
        conn = self.conn

        Id = input("请输入您要更新的留言内容的ID:")
        try:
            # 查询有效留言的id
            sql = """select message_pad.id from for_study.message_pad where message_pad.is_deleted = 0;"""
            cursor.execute(sql)
            results = cursor.fetchall()  # 输出样例 : [{'id': 1}, {'id': 10}]
        except Exception as e:
            print(type(e), ':', e)
        if {'id': int(Id)} in results:
            try:
                print("原留言:")
                self.search(int(Id))
            except Exception as e:
                print("原留言查询失败!")
                print(type(e), ':', e)

            new_message = input("请输入您要重新书写的留言内容:")

            sql = """UPDATE for_study.message_pad SET `message` = '%s'  WHERE (`id` = %s);
    """ % (new_message, Id)
            # print(sql)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 执行sql语句
                conn.commit()
                print("更新成功!")
            except Exception as e:
                print(type(e), ':', e)
                # 发生错误时回滚
                conn.rollback()

        else:
            print("您所选的ID不存在或其记录已被删除!")

    def delete(self):
        """
        删
        """
        cursor = self.cursor
        conn = self.conn
        Id = input("请输入您要删除留言的ID:")
        # self.search(Id)
        try:
            sql = """select message_pad.id from for_study.message_pad where message_pad.is_deleted = 0;"""
            cursor.execute(sql)  # 返回有效留言的id
            results = cursor.fetchall()  # 样例 : [{'id': 1}, {'id': 10}]
        except Exception as e:
            print(type(e), ':', e)
        if {'id': int(Id)} in results:
            # SQL 删除语句
            #         sql = """DELETE  FROM for_study.message_pad Where `id` = %s;
            # """ % (Id)
            # 此时的删除,只需要将is_deleted置为1
            sql = """UPDATE for_study.message_pad  SET message_pad.is_deleted = 1 WHERE message_pad.id =%s;
            """ % (Id)
            # print(sql)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 执行sql语句
                conn.commit()
                print("删除成功!")
            except Exception as e:
                print(type(e), ':', e)
                # 发生错误时回滚
                conn.rollback()
        else:
            print("您所选的ID不存在或其记录已被删除!")

class menu():
    print("欢迎访问留言板✪ ω ✪")
    # 改为使用我的云数据库
    db = database(host='rm-2zeboe0v5sp4jl2j81o.mysql.rds.aliyuncs.com', user='visitor', passwd='Visitor123',
                  db='for_study')
    while True:
        print("""
|--------------------------------------
|   显示所有留言请键入：1                
|   查询留言请键入：2                   
|   留言请键入：3                        
|   修改留言内容请键入：4                 
|   删除留言请键入：5                    
|   退出请键入：0                        
|--------------------------------------""")
        choice = input("您的选择:")
        if choice == '0':
            db.exit()
            print("已退出,祝您生活愉快（￣︶￣）↗　")
            break
        elif choice == '1':
            db.search()
        elif choice == '2':
            Id = int(input("请输入您要查看的留言id:"))
            db.search(Id)
        elif choice == '3':
            db.append()
        elif choice == '4':
            db.update()
        elif choice == '5':
            db.delete()
        else:
            continue

if __name__ == "__main__":
    menu()

