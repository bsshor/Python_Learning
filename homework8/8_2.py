# -*- encoding: utf-8 -*-
'''
@File : 8_2.py
@Time : 2020/04/28 00:11:01
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    给定一组数据网址数据，请判断这些网址是否可以访问； 
    用多线程的方式来实现
'''
"""
在思考一个问题:
因为资源(每行网址)是有限的,不能重复访问的.
那么如果不对资源加锁,则会产生重复访问!

如果对资源加锁,提高了安全性,却使得程序变成了串行的,
失去了使用多线(进)程的意义!

可以肯定过的是,必须是要保证资源的安全性,
这种牺牲了速度带来的安全又违背了使用多线(进)程的本意---提高执行效率

所以,矛盾出现'锁'上了,本质是安全访问(或有效访问)和效率的矛盾
怎么 解决呢?
---IPC通信机制：队列和管道。
队列和管道都是将数据存放于内存中，队列又是基于（管道+锁）实现的，可以让我们从复杂的锁问题中解脱出来，
我们应该尽量避免使用共享数据，尽可能使用消息传递和队列，避免处理复杂的同步和锁问题，而且在进程数目增多时，往往可以获得更好的可扩展性。

需要牺牲内存~
"""


# here put the import lib
import threading
from concurrent.futures import ThreadPoolExecutor
import queue
import time
import requests
def resource():
    """
    读取文件里的网址资源,创建消息队列
    """
    resource = queue.Queue()
    with open(r'homework8\url_data.txt', 'r') as fr:
        line = fr.readline()
        while line:
            resource.put(line)
            line = fr.readline()
    return resource


def getHtmlText(queue):
    while not queue.empty():
        try:        # 网络连接有风险，异常处理很重要
            n = queue.qsize()
            urls = queue.get().strip()  # 去除'\n'
            urls = urls.split(';')
            for url in urls:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
                r = requests.get(url, headers=headers,
                                 timeout=2)    # 查一下这个方法的使用
                r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
                print(n, ': ', url, ':200')
        except:
            print(n, ': ', url, ':', r.status_code)


if __name__ == "__main__":
    start1 = time.time()
    re = resource()
    end1 = time.time()

    start2 = time.time()
    with ThreadPoolExecutor(30) as executor:  # 容量为 30 的线程池
        for i in range(100):  # 开了100个线程
            executor.submit(getHtmlText, re)
    end2 = time.time()
    print("构建队列用时: "+str(end1-start1) + 's')  # 0.002~0.003
    print("判断网址用时: "+str(end2-start2) + 's')  # 四百秒左右左右
