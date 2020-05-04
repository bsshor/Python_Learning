# -*- encoding: utf-8 -*-
'''
@File : server9_4.py
@Time : 2020/05/03 12:07:28
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    设计一款能实现多人聊天的系统：使用socket和多线程技术，
编写全多人聊天室
------服务器部分
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


class ChatSever:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (get_ip(), 10000)
        self.users = {}

    def start_sever(self):
        try:
            self.sock.bind(self.addr)
        except Exception as e:
            print(e)
        self.sock.listen(5)
        print("服务器已开启，等待连接...")
        print("在空白处输入stop sever并回车，来关闭服务器")

        self.accept_cont()

    def accept_cont(self):
        while True:
            s, addr = self.sock.accept()
            self.users[addr] = s
            number = len(self.users)
            print("用户{}连接成功！现在共有{}位用户".format(addr, number))

            threading.Thread(target=self.recv_send, args=(s, addr)).start()
            
    def recv_send(self, sock, addr):
        while True:
            try:  # 测试后发现，当用户率先选择退出时，这边就会报ConnectionResetError
                response = sock.recv(4096).decode("gbk")
                msg = "{}用户{}发来消息：{}".format(get_time(), addr, response)

                for client in self.users.values():
                    client.send(msg.encode("gbk"))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.users.pop(addr)
                break

    def close_sever(self):
        for client in self.users.values():
            client.close()
        self.sock.close()
        os._exit(0)


if __name__ == "__main__":
    # print(get_ip())
    sever = ChatSever()
    sever.start_sever()
    while True:
        cmd = input()
        if cmd == "stop sever":
            sever.close_sever()
        else:
            print("输入命令无效，请重新输入！")
    
