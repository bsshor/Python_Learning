# -*- encoding: utf-8 -*-
'''
@File : 9_3.py
@Time : 2020/05/01 19:25:40
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答
'''

# here put the import lib

import socket

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#  准备接收方的地址
dest_addr = ('192.168.29.1', 8888)
print("双方输入   \exit   均可结束通信  ")
while True:
    # 发送数据:
    send = input('>>')
    if send == '\exit':
        break
    s.sendto(bytes(send.encode('gbk')), dest_addr) 
    # 接收数据:
    recive = s.recv(1024).decode('gbk')
    if recive == '\exit':
        break
    print('->', recive)
print("结束通信")

s.close()