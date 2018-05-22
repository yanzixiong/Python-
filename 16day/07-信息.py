from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.sendto('98K带你吃鸡'.encode('gb2312'),('172.20.10.5',8080))


s.close()
