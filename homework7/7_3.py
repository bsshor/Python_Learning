# -*- encoding: utf-8 -*-
'''
@File : 7_3.py
@Time : 2020/04/20 15:49:14
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
给定一个网址（包含了优质的英语学习音频文件):http://www.listeningexpress.com/studioclassroom/ad/ 
请大家写一个爬虫，将里面的英语节目MP3，都下载下来
'''
# here put the import lib
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
"""
经本人研究此网站的代码,发现:
<a href="javascript:p('sc-ad 2020-04-15 Insights on Entertainment.mp3');">(高级) 2020-04-15 Insights on Entertainment.mp3</a>
在这里有一个javascript:p()函数限定了网页的跳转,真正的链接在函数里
另外,空格会被默认为命令分隔符,需要进行url编码
真正有效的超链接如下所示:
<source src="http://www.listeningexpress.com/studioclassroom/ad/sc-ad%202020-04-14%20Insights%20on%20Entertainment.mp3" type="audio/mpeg">
仔细观察,可以发现异同,只需要在把从js函数里获取的链接里的空格替换成'%20'即可
或者用urllib.parse.quote()直接编译成url
"""


def get_name(start_url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
        origin_url = start_url
        response = requests.get(origin_url, headers=headers, timeout=2)
        print(origin_url, ':', response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.find_all('a')  # 获取超链接文本
        names = []
        for text in texts:
            # print(text['href']) # 类型为str
            # 发现一个细节问题:
            # <a href="javascript:p('sc-ad 2020-04-23 It\'s Cool to Care.mp3');"> ...</a>
            # 文件名在html里多了一个'\'转置符号,需要处理
            url1 = re.search('\'[a-zA-Z0-9- \.\'mp3]*',
                            text['href'].replace('\\', ''))
            # 匹配出来的是这种类型'sc-ad 2020-04-23 It's Cool to Care.mp3'
            if url1:
                url2 = url1.group().strip('\'')  # 去掉两边的单引号
                # 匹配出文件名:2020-04-23 It's Cool to Care.mp3
                na2 = re.search('[0-9]{3}[-0-9\w\s\'$.mp3]*', url2)
                names.append(na2.group())
    except Exception as e:
        print(type(e), ':', e)
    return names


def get_resource(start_url, names):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    for name in names:
        try:
            with open(r'homework7\MP3\{}'.format(name), 'wb') as fw:
                target_url = start_url + quote('sc-ad ' + name)  # 转换成超链接
                # 此处 quote(name) = name.replace(' ', "%20")
                print(target_url)
                response = requests.get(target_url, headers=headers, timeout=2)
                fw.write(response.content)
        except Exception as e:
            print(type(e), ':', e)


if __name__ == '__main__':
    url = r'http://www.listeningexpress.com/studioclassroom/ad/'
    names = get_name(url)
    get_resource(url, names)
    print("下载结束!")
