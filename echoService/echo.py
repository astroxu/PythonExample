# echoService，接收数据并将接收到的数据返回
# -*- coding:utf-8 -*-

from _socket import *

# 1.创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 2.绑定本地相关信息，如果一个网络程序不绑定，则系统会随机分配
bindAddr = ('', 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udpSocket.bind(bindAddr)

num = 1
while True:
    # 3.等待接收方发送的数据
    recvData = udpSocket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    # content, destInfo = recvData

    # 4.将接收到的数据再发送给对方
    udpSocket.sendto(recvData[0], recvData[1])

    # 5.统计信息
    print("已经将接收到的第%d个数据返回给对方，内容为：%s" % (num, recvData[0]))
    num += 1

# 6.关闭套接字
udpSocket.close()
