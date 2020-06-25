#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : config.py
@Time : 2020/6/24 17:31:11 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
配置模块
"""

DEBUG = True

# 数据库连接定义
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'visitor'
PASSWORD = 'Visitor123'
HOST = 'rm-2zeboe0v5sp4jl2j81o.mysql.rds.aliyuncs.com'  # 数据存放于阿里云
PORT = '3306'
DATABASE = 'for_study'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 初始化连接池的容量
POOL_SIZE = 10

# 连接池的最大溢出容量
MAX_OVERFLOW = 20

# 最大溢出容量 + 初始化容量 = 最大容量，超出这个最大值，数据库就会堵塞。并等待30s（timeout = 30，默认）
