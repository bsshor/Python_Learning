## exe7 Python 正则表达式及网络爬虫练习题

[作业地址](https://note.youdao.com/ynoteshare1/index.html?id=365ba9d1f85c739bc317577af1dfc374&type=note)

#### 关于爬虫的相关知识，大家参考我们后续的课程内容

文档：13 网络爬虫

链接：<http://note.youdao.com/noteshare?id=a15adcaebaf739f4ebc69f4c574327ee>



### 1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；

   提示，文件有1000行，注意控制每次读取的行数；

​    给定文件:webspiderUrl.txt  (自行从作业地址里下载)

7_1.py

文件输出在 Url.txt



### 2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；

​    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；

​    提示：要用到requests库，BeautifulSoup库
7_2.py

文件输出在Introduction.txt




### 3  给定一个网址（包含了优质的英语学习音频文件），<http://www.listeningexpress.com/studioclassroom/ad/>；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；

​     这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：

![img](https://note.youdao.com/yws/public/resource/365ba9d1f85c739bc317577af1dfc374/xmlnote/B42CD4A7D5F94820AAE29F735E8D5C9A/27574)

   要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；

  Windows上的wget可以[点击这里](https://eternallybored.org/misc/wget/1.19.4/32/wget.exe) 下载。 这个程序不用安装，直接在命令行里使用即可；

注意：

- 获取的音频网址前面需要加上 前缀 http://www.listeningexpress.com/studioclassroom/ad/ 才是完整的下载地址
- MP3文件中有空格字符，组成下载网址时，需要进行url编码，否则空格会被当成命令行分隔符。参考代码如下所示

\>>> from urllib.parse import quote>>> quote('2019-04-13 NEWSworthy Clips.mp3')'2019-04-13%20NEWSworthy%20Clips.mp3'

7_3.py

文件输出在MP3文件夹




### 4 爬取这个网址上<http://www.python3.vip/doc/prac/python/0001/>，所有的Python练习题题目和答案；保存到txt文件中（只保留文字）；

​    文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：

![img](https://note.youdao.com/yws/public/resource/365ba9d1f85c739bc317577af1dfc374/xmlnote/BC457B2D15C64451AF0579B18A353FE9/27596)

  参考文档：<https://blog.csdn.net/weixin_43687366/article/details/88877996>

   大家看完这篇文档后，再开始动手做这道题；

7_4.py

文件输出在Exercises and analysis.txt