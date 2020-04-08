# -*- encoding: utf-8 -*-
'''
@File : 5_2.py
@Time : 2020/04/08 00:48:14
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    编写一个装饰器，能记录其他函数调用的日志，
将日志写入到文件中
'''

# here put the import lib

import traceback
import logging
from logging.handlers import TimedRotatingFileHandler


def logger(func):
    def inner(*args, **kwargs):  
        try:
            func(*args, **kwargs)  
        except:
            print('error')
    return inner


def loggerInFile(filename):  # 带参数的装饰器需要2层装饰器实现,第一层传参数，第二层传函数，每层函数在上一层返回
    def decorator(func):
        def inner(*args, **kwargs):  # 第一层
            logFilePath = r'homework5\newloglog' # 日志按日期滚动，保留5天
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            handler = TimedRotatingFileHandler(logFilePath,when="d",
                                                interval=1,
                                                backupCount=5)
            formatter = logging.Formatter(
                '%(asctime)s  - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            try:
                result = func(*args, **kwargs)  # 第2层
                logger.info(result)
            except:
                logger.error(traceback.format_exc())
        return inner
    return decorator


@logger
def A():
    print("你好")


A()


@loggerInFile(r'homework5\newloglog') #@loggerInFile(r'homework5\newloglog')
def B(n):
    print(100/n)


B(100)
B(0)
B(3)
