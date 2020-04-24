#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 7_2.py
@Time : 2020/4/20 00:16:42 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
给定100个企业网站首页链接地址（用1中给出的URL地址）；
请爬取每个页面上，企业介绍的链接地址；
说明，满足企业介绍网址的条件是，
标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
提示：要用到requests库，BeautifulSoup库
"""
# here put the import lib
import requests
import re
from bs4 import BeautifulSoup


with open(r'G:\桌面\Python_Learning\homework7\Url.txt', 'r', encoding='utf-8') as fr:
    effective = 0  # 经查，第一题中给的很多网址是无效网址，此处用effective记录有效的网址数目，满100退出
    # 为了避免被待爬取网页禁止爬取，增加请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    pattern = "(走进.*)|(关于我们)|((企业|公司)(介绍|概况|发展))|(发展历史)"

    while effective < 100:
        orign_url = fr.readline().strip()
        try:
            response = requests.get(orign_url, headers=headers, timeout=2)
            if response.status_code == 200:  # 如果orign_url有效，则effective进1
                effective += 1
                print(effective, '  ', orign_url, ':', response.status_code)

            soup = BeautifulSoup(response.content, 'html.parser')
            texts = soup.find_all('a')  # 筛出所有超链接
            # print(type(texts)) # 返回的类型是<class 'bs4.element.ResultSet'>
            # print(texts)
            for text in texts:   # text 的类型依然是<class 'bs4.element.Tag'>
                # print(type(text),text)
                # 匹配是否有符合要求的可能链接
                if re.search(pattern, text.text):
                    if 'href' in str(text):  # 判断是否有url，需要转换成字符串类型判断
                        print("href:>>>>", text.attrs['href'])
                        target_url = orign_url.rstrip('/')+'/'+text.attrs['href'].lstrip('/')  # 拼接url
                        with open(r"G:\桌面\Python_Learning\homework7\Introduction.txt", "a", encoding="utf-8") as fw:
                            fw.write(target_url+'\n')

        except Exception as identifier:
            print(orign_url, "failed")
