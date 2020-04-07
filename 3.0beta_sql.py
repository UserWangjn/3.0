#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 导入模块
import paramiko
import time
import socket
import os
import submit
import json


def con_linux(hostname,ports,username,password):

    print hostname,ports,username,password
    s=paramiko.SSHClient()
    # 取消安全认证
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接linux
    Flag=False

    while not Flag:
      try:
        s.connect(hostname=hostname,port=ports,username=username,password=password)
        print("连接中……")
        con=1
      except socket.gaierror,e:
        print 'Error connecting to server: %s' % e
        time.sleep(2)
        continue
      Flag = True
    # 执行命令
    print "已连接……"

    stdin,stdout,stderr=s.exec_command("cd /opt/tingyun/mysql/bin")
    stdin,stdout,stderr=s.exec_command("./mysql -ulens -p")
    stdin,stdout,stderr=s.exec_command("show databases")
    result=stdout.read()
    print(result)
    print()







print con_linux(hostname='10.129.4.12',ports=22,username='tingyun',  password='nbs2010')#调用模块，传入liunx的ip/用户名/密码，并打印返回结果



