# -*- encoding: utf-8 -*-
'''
@File : cilent9_4.py
@Time : 2020/05/03 12:07:38
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    设计一款能实现多人聊天的系统：使用socket和多线程技术，
编写全多人聊天室
------客户端部分
'''

# here put the import lib

import socket
import threading
import os
import datetime


def get_ip():
    """用来搞到IP"""
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip


def get_time():
    """得到发送时间"""
    now = datetime.datetime.now()
    send_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return send_time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('39.96.113.12', 10000)
# 服务器端的IP和端口
# addr = (get_ip(), 10000)
# 只有自己一台电脑做测试时，可以直接用左边的
s.connect(addr)

def recv_msg():  #
    print("连接成功！现在可以接收消息！\n")
    while True:
        try:  # 测试发现，当服务器率先关闭时，这边也会报ConnectionResetError
            response = s.recv(1024)
            print(response.decode("gbk"))
        except ConnectionResetError:
            print("服务器关闭，聊天已结束！")
            s.close()
            break
    os._exit(0)


def send_msg():
    print("连接成功！现在可以发送消息！\n")
    print("输入消息按回车来发送")
    print("输入esc来退出聊天")
    while True:
        msg = input()
        if msg == "esc":
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode("gbk"))
    os._exit(0)


threads = [threading.Thread(target=recv_msg), threading.Thread(target=send_msg)]
for t in threads:
    t.start()
