#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 10_3.py
@Time : 2020/5/9 09:34:20 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
对2中的表结构，用SQLAchemy模块来实现同样的操作
"""
import datetime

# 创建表中的字段(列)
from sqlalchemy import Column
from sqlalchemy import String, INTEGER, Text, DateTime
# 创建连接相关
from sqlalchemy import create_engine
# 和 sqlapi 交互，执行转换后的 sql 语句，用于创建基类
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# 创建对象的基类:
Base = declarative_base()


# 定义Message_Pad对象:
class Message_Pad(Base):
    # 表的名字:
    __tablename__ = 'message_pad'

    # 表的结构:
    id = Column(INTEGER, primary_key=True)
    message = Column(Text)
    author = Column(String(45))
    time = Column(DateTime, default=datetime.datetime.now())
    is_deleted = Column(INTEGER, default=0)


class sqlalchemy():
    def __init__(self):
        """
        初始化数据库连接,创建会话
        """
        try:
            # 创建连接对象，并使用 pymsql 引擎
            self.engine = create_engine(
                'mysql+pymysql://visitor:Visitor123@rm-2zeboe0v5sp4jl2j81o.mysql.rds.aliyuncs.com:3306/for_study')

            # 创建DBSession类型:
            self.DBSession = sessionmaker(bind=self.engine)

            # 创建Session:
            self.session = self.DBSession()

        except Exception as e:
            print(type(e), ':', e)

    def search_all(self):
        """
        查询所有未被删除的留言
        :return:
        """
        try:
            session = self.session
            all_messages = session.query(Message_Pad).filter(Message_Pad.is_deleted == 0).all()

            for message in all_messages:
                print('-' * 50)
                print('id:', message.id, '\t', '日期:', message.time)
                print('留言:', message.message)
                print('姓名:', message.author)
                print('-' * 50)

        except Exception as e:
            print(type(e), ':', e)

    def serch_one(self):
        """
        查询某一条未被删除的留言
        :return:
        """
        try:
            session = self.session
            Id = input("请输入您要查询的留言的id:")
            # 多条件查询
            # message = session.query(Message_Pad).filter(Message_Pad.id == Id, Message_Pad.is_deleted == 0).one()
            message = session.query(Message_Pad).filter_by(id=Id).filter(Message_Pad.is_deleted == 0).first()
            if message == None:  # 若查询结果为空,其值为None,类型是NoneType
                print("此留言不存在或已被删除!")
            else:
                print('id:', message.id, '\t', '日期:', message.time)
                print('留言:', message.message)
                print('姓名:', message.author)
        except Exception as e:
            print(type(e), ':', e)

    def append(self):
        """
        写留言
        :return:
        """
        try:
            session = self.session
            text = input("请输入您的留言内容:")
            author = input("请署名:")
            new_message = Message_Pad(message=text, author=author)
            # 添加到session
            session.add(new_message)
            # 提交
            session.commit()
            print("留言成功!")
        except NoResultFound:
            print("您所选的留言不存在")
        # except Exception as e:
        #     print(type(e), ':', e)

    def update(self):
        """
        改留言
        :return:
        """
        try:
            session = self.session

            Id = input("请输入您要更改的留言的id:")
            # 多条件查询
            # message = session.query(Message_Pad).filter_by(Message_Pad.id == Id, Message_Pad.is_deleted == 0).one()
            message = session.query(Message_Pad).filter_by(id=Id).filter(Message_Pad.is_deleted == 0).first()
            if message == None:  # 若查询结果为空,其值为None,类型是NoneType
                print("此留言不存在或已被删除!")
            else:
                text = input("请输入您的新留言:")
                message.message = text
                session.commit()
                print("更新成功!")

        except Exception as e:
            print(type(e), ':', e)

    def delete(self):
        """
        此处的删除仅是将is_delete置为1
        :return:
        """
        try:
            session = self.session
            Id = input("请输入您要删除的留言的id:")
            # 多条件查询
            message = session.query(Message_Pad).filter_by(id=Id).filter(Message_Pad.is_deleted == 0).first()
            # print(type(message))
            if message is None:  # 若查询结果为空,其值为None,类型是NoneType
                print("此留言不存在或已被删除!")
            else:
                message.is_deleted = 1
                session.commit()
                print("删除成功!")
        except Exception as e:
            print(type(e), ':', e)

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self.session.close()


class menu():
    alchemy = sqlalchemy()
    print("欢迎访问留言板✪ ω ✪")
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
            alchemy.close()
            print("已退出,祝您生活愉快（￣︶￣）↗　")
            break
        elif choice == '1':
            alchemy.search_all()
        elif choice == '2':
            alchemy.serch_one()
        elif choice == '3':
            alchemy.append()
        elif choice == '4':
            alchemy.update()
        elif choice == '5':
            alchemy.delete()
        else:
            continue


if __name__ == '__main__':
    menu()

"""
# 该段存在  NameError: name 'Message_Pad' is not defined  的问题,莫名其妙,极其玄乎

from sqlalchemy import Column, INTEGER, Text, String, DateTime
import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Message(declarative_base()):
    __tablename__ = 'message_pad'

    id = Column(INTEGER, primary_key=True)
    message = Column(Text)
    author = Column(String(45))
    # time = Column(DateTime, default=datetime.datetime.now())
    is_deleted = Column(INTEGER, default=0)

    # time = Column(TIMESTAMP, nullable=False, comment='更新时间戳',server_default=Text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    # time = Column(TIMESTAMP, server_default=Text('CURRENT_TIMESTAMP'), server_onupdate=Text('CURRENT_TIMESTAMP'))  # 格式为时间戳
    # time =Column(TIMESTAMP, nullable=False, comment='更新时间戳',
    #                    server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    from sqlalchemy import create_engine

    engine = create_engine(
        'mysql+pymysql://visitor:Visitor123@rm-2zeboe0v5sp4jl2j81o.mysql.rds.aliyuncs.com:3306/for_study')

    from sqlalchemy.orm import sessionmaker

    # 把当前引擎绑定给这个会话
    Session = sessionmaker(bind=engine)
    # 实例化
    session = Session()
    mes = session.query(Message).all()
    ret = engine.execute('select * from message_pad;')
    print(ret)
    for i in mes:
        print('-' * 50)
        print(i.id, )
        print(i.author, i.message)
        print('-' * 50)
"""
