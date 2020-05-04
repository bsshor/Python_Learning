
# -*- encoding: utf-8 -*-
'''
@File : 9_2.py
@Time : 2020/05/01 17:24:54
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    编写一个接收数据的网络程序，
由“网络调试工具”发送数据，
你的程序接收数据并打印输出
'''

# here put the import lib
from socket import *

def main():
   # 绑定端口信息
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    
    local_addr=('192.168.29.1',9999)

    udp_socket.bind(local_addr)
   # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        if recv_data[0].decode('GBK') == 'exit':
            break
        # 打印显示接收到的数据
        print(recv_data[0].decode('utf8'))

   # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()