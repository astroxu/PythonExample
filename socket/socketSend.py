#socket接收
# -*- coding:utf-8 -*-

from _socket import *

# 1.创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 2.准备接收方地址
sendAddr = ('192.168.43.115', 7788)

# 3.从键盘获取数据
sendData = input("请输入要发送的数据：")

# 4.发送数据到指定的电脑上
#udpSocket.sendto(b"haha", sendAddr) #python3发送socket数据需要将字符串前加b
udpSocket.sendto(sendData.encode("utf-8"), sendAddr) #设置编码格式
# 5.关闭套接字
udpSocket.close()
