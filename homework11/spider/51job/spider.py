#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : spider.py
@Time : 2020/6/20 22:45:37
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
数据爬取模块
"""
import queue
import re
import time
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup

import Model.model as model

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                       AppleWebKit/537.36 (KHTML, like Gecko)\
                       Chrome/81.0.4044.138 Safari/537.36'
}


def Get_Pages():
    """
    1.提取页码
    2.构造队列
    :return:
    """
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99," \
          "python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html "

    try:
        html = requests.get(url, headers=header, timeout=20)
        html.encoding = 'gbk'

        # 提取页码
        soup = BeautifulSoup(html.content, 'html.parser')
        td = soup.find_all('span', class_="td")
        length = re.search(r'\d+', td[0].text)

        length = int(length.group())  # 得到页码长度

        # 为下一步的多线程做准备
        # 将页号视作被竞争资源，依次存入队列中
        pages = queue.Queue(length)
        for i in range(1, length + 1):
            pages.put(i)

        return pages

    except Exception as e:
        print(type(e), ':', e)


def web(pages):
    """
    数据爬取
    :param pages:
    :return:
    """

    url = 'https://search.51job.com/list/00000,000000,0000,00,9,99,' \
          'python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html'.format(
        pages.get())  # 临界资源出队列

    # print(url)  # 输出拼接后的url
    html = requests.get(url, headers=header, timeout=20)
    html.encoding = 'gbk'
    soup = BeautifulSoup(html.content, 'html.parser')

    resultList = soup.find_all(name="div", attrs={'class': 'dw_table', 'id': 'resultList'})
    els = resultList[0].find_all(name="div", attrs={'class': 'el'})
    positions = []
    for el in els[1:]:
        position = []
        t1 = el.find_all('p', class_='t1')
        t11 = t1[0].find_all('span')
        position.append(t11[0].text.strip())
        t2 = el.find_all('span', class_='t2')
        position.append(t2[0].text)
        t3 = el.find_all('span', class_='t3')
        position.append(t3[0].text)
        t4 = el.find_all('span', class_='t4')
        position.append(t4[0].text)
        t5 = el.find_all('span', class_='t5')
        position.append(t5[0].text)
        positions.append(position)

    # 数据存入数据库
    model.Jobs.append(positions)


def Spider_51job():
    """
    1.多线程爬取（构造线程池）
    2.信息插入数据库
    :return:
    """
    pages = Get_Pages()
    length = pages.qsize()

    start2 = time.time()
    with ThreadPoolExecutor(30) as executor:  # 容量为 15 的线程池
        for i in range(length):  # 开了个线程
            executor.submit(web, pages)
    end2 = time.time()
    print("数据爬取+数据库插入总用时: " + str(end2 - start2)[:5] + 's')  # 23s左右

if __name__ == '__main__':
    Spider_51job()



