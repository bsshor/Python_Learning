# -*- encoding: utf-8 -*-
'''
@File : 7_4.py
@Time : 2020/04/21 16:16:31
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
爬取这个网址上<http://www.python3.vip/doc/prac/python/0001/>，
所有的Python练习题题目和答案；保存到txt文件中（只保留文字）；
​文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote

def get_url(url):
    """
    获得所有习题链接
    """
    orign_url = url
    headers =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
    response = requests.get(orign_url, headers = headers, timeout = 2)
    print(orign_url, ':', response.status_code)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    re_a = soup.find(id="main").ul.find_all('a')
    links = []
    for a in re_a:
        links.append(a.attrs['href'])
    return links

def get_content(links):
    """
    
    """
    for link in links:
        
        dict = {}
        headers =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
        response = requests.get(link, headers = headers, timeout = 2)
        if response.status_code == 200:
            print(link, ':200')
            soup = BeautifulSoup(response.content, 'html.parser')
            dict['title'] = soup.find(id="main").h1.text # 获取标题
            
            # dict['tm'] = soup.find(id='main').find_all('p')[2].text # 查找题目
            # print(dict)
            re_a = soup.find(id='main').find_all('p')
            
            #print(re_b)

            with open(r'G:\桌面\Python_Learning\homework7\Exercises and analysis.txt','a',encoding='utf-8') as fw:
                fw.write(">>>" + dict['title'] + '\n')
                for text in re_a:
                    con = text.text
                    # if con == "答案与解析":
                    #     answer = link + text.find('a').attrs['href']
                    if con:
                        fw.write(con + '\n')
                answer = link + '#题目1-答案'
                fw.write(">>答案与解析\n")
                res = requests.get(answer, headers = headers, timeout = 2)
                if res.status_code == 200:
                    soup = BeautifulSoup(res.content, 'html.parser')
                    re_b = soup.find(id='main').find_all('p')
                    for te in re_b:
                        co = te.text
                        if co:
                            fw.write(co + '\n')
                    print("成功")
                
                
                    
            

                    
                    
            #print(link,dict)
            
        else:
            print(link, ':', response.status_code)



if __name__ == "__main__":
    url = 'http://www.python3.vip/doc/prac/python/0001/'
    urls = get_url(url)
    #print(urls)
    get_content(urls)