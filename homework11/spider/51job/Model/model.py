#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : model.py
@Time : 2020/6/20 22:43:37
@Author : Bundchen
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
数据库模块
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import or_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

Base = declarative_base()
metadata = Base.metadata


class Python51job(Base):
    __tablename__ = 'python_51job'

    id = Column(Integer, primary_key=True)
    job = Column(String(255))
    company = Column(String(255))
    place = Column(String(255))
    salary = Column(String(255))
    release_time = Column(String(255))


class Jobs():
    try:
        # 创建连接对象，并使用 mysqlconnector 引擎
        engine = create_engine(
            config.SQLALCHEMY_DATABASE_URI, pool_size=config.POOL_SIZE, max_overflow=config.MAX_OVERFLOW)

        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)




    except Exception as e:
        print(type(e), ':', e)

    @classmethod
    def search_all(cls):
        try:
            # 创建专属session
            session = cls.DBSession()

            salaries = session.query(Python51job.salary).filter(not_(Python51job.salary == '')).filter(
                Python51job.place.like('%北京%')).filter(
                or_(Python51job.salary.like('%万/月%'), Python51job.salary.like('%千/月%')))
            session.close()

            return salaries
        except Exception as e:

            print(type(e), ':', e)

    @classmethod
    def append(cls, positions):
        try:
            # 创建专属session
            session = cls.DBSession()
            for position in positions:
                session.add(Python51job(job=position[0], company=position[1], place=position[2], salary=position[3],
                                        release_time=position[4], ))
                session.commit()

            session.close()
            return 'success！'
        except Exception as e:
            print(type(e), ':', e)



