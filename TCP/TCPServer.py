# -*- coding:utf-8 -*-

from _socket import *

#创建socket
tcpSerSocket = socket(AF_INET,SOCK_STREAM)

#绑定
address = ('',8899)
tcpSerSocket.bind(address)

#使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的
tcpSerSocket.listen(5)

#如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
#newSocket用来为这个客户端服务
#tcpSerSocket就可以省下来专门等待其他新的客户端的链接
newSocket,clientAddr = tcpSerSocket._accept()

#接收对方发送过来的数据，最大接收1024字节
recvData = newSocket.recv(1024)
print("接收到的数据为：",recvData)

#发送一些数据到客户端
newSocket.send("thank you !")

#关闭为这个客户端服务的套接字，只要关闭了，就意味着不能再为这个客户端服务
newSocket.close()

#关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端
tcpSerSocket.close()