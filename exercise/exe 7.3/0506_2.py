# -*- encoding: utf-8 -*-
'''
@File : 0506_2.py
@Time : 2020/05/06 17:45:43
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    创建一个留言板的表（ID，留言主题，留言人，留言时间）4个字段，注意，字段请用英文；
完成对这个表记录的增，删，改，查询；
用PyMySQL驱动方式
'''

# here put the import lib
import pymysql
import datetime
def get_time():
    """
    获取当前日期时间
    """
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time


class database():
    def __init__(self, host='localhost', user='root', passwd='root',  db='', charset='utf8'):
        # 建立连接 
        self.conn = pymysql.connect(host=host,user=user, passwd=passwd, db=db, charset=charset)
        # 创建游标，操作设置为字典类型        
        self.cursor = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def exit(self):

        self.cursor.close()
        self.conn.close()

    
    def create(self):
        """
        创建
        """
        cursor = self.cursor
        sql = """
CREATE TABLE `my_test`.`message` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `theme` TEXT NULL,
  `author` VARCHAR(45) NULL,
  `time` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
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
        time = get_time()
        # SQL 插入语句
        sql = """INSERT INTO `my_test`.`message` (`theme`, `author`, `time`)
        VALUES (\'%s\',\'%s\',\'%s\');""" % (theme, name, time)
        # print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
                # 执行sql语句
            conn.commit()
        except:
            # 发生错误时回滚
            conn.rollback()
        # #----------------------------------------------
        # # 关闭游标
        # cursor.close()
        # # 关闭数据库连接
        # conn.close()
        # #----------------------------------------------
        # #>>实践证明,此处既不能关闭游标,也不能关闭数据库连接
        print("留言成功!")

    def search(self,Id = None):
        """
        查
        """
        cursor = self.cursor
        if Id == None:
            sql = 'SELECT * FROM my_test.message;'
        else:
            sql = 'SELECT * FROM my_test.message where id = %d;'%Id
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        # 查询结果是一个列表,元素为由行组成的字典
        # 字典的键和值分别是每个列的列名和对应的内容
        for row in results:
            Id = row['id']
            message = row['theme']
            name = row['author']
            time = row['time']
            print('-'*100)
            print(Id,'  ',time,'    ')
            print(name,':',message)
            print('-'*100)

    def update(self):
        """
        改
        """
        cursor = self.cursor
        conn = self.conn
        # theme = input("请输入您要留言的内容:")
        # name = input("请留下您的姓名:")
        # time = get_time()
        #database.search()
        Id = input("请输入您要更新的留言内容的id:")
        #database.search(Id)
        theme = input ("请输入您要重新书写的留言内容:")
        time = get_time()
        # SQL 插入语句
        sql = """UPDATE `my_test`.`message` SET `theme` = '%s', `time` = '%s' WHERE (`id` = %s);
""" % (theme, time, Id)
        # print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
                # 执行sql语句
            conn.commit()
        except:
            # 发生错误时回滚
            conn.rollback()
        print("更新成功!")

    def delete(self):
        """
        删
        """
        cursor = self.cursor
        conn = self.conn
        Id = input("请输入您要删除留言的id:")
        #database.search(Id)
        
        # SQL 插入语句
        sql = """DELETE  FROM my_test.message Where `id` = %s;
""" % (Id)
        # print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
                # 执行sql语句
            conn.commit()
        except:
            # 发生错误时回滚
            conn.rollback()
        print("删除成功!")


if __name__ == "__main__":
    db = database(passwd='sbs5218',db= 'my_test')
    #db.create()
    #for i in range(10):
    db.append()
    db.search()
    db.update()
    db.delete()
    db.exit()
    
    
