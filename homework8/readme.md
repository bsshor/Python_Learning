## exe8 Python多任务练习题

[作业地址](https://note.youdao.com/ynoteshare1/index.html?id=3851b0ef7da7d113e9a8d9ca4f3f48e6&type=note)

### 1  有100个同学的分数：数据请用随机函数生成；

​     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；

​     B 利用线程池来实现；

8_1.py

### 2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；

   请查资料，Python的 requests库，如何判断一个网址可以访问；

提示 ：使用requests模块

   def getHtmlText(url):

​    try:        # 网络连接有风险，异常处理很重要

​        r = requests.get(url,timeout=30)    # 查一下这个方法的使用

​        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常

​        r.encoding = r.apparent_encoding

​        return r.text

​    except:

​         return "产生异常"

  数据文件（1000个网址）：url_data.txt

8_2.py

### 3  多进程练习：

计算1～100000之间所有素数的个数， 要求如下:

\- 编写函数判断一个数字是否为素数，然后统计素数的个数；

-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。

-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。

8_3.py

### 4 多进程通讯：

  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息

8_4.py