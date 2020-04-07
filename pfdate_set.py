#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YIMAO'
import time

# DC_HOST="http://beaconalpha1.tingyun.com/pf?"        #内网
# DC_HOST="http://beaconalpha1.tingyun.com"
# DC_HOST="http://beaconbeta.tingyun.com/pf?"            #beta
DC_HOST="http://beacon.tingyun.com/"              #外网


# apdex
cachetime=1   #缓存时间
jsErrorRate=0.1 #js错误率
serverResponseTime=1000 #服务器响应时间
pagePrint=10 #页面渲染
pagePrint=pagePrint-1
# htmlLoadTime=1 # Html加载时间
dnsTime=10 # dns
domRedayTime=10 #  可交互
fristPaintTime=10 # 首次渲染&白屏
firstScreenTime=10 #首屏
#loadtime=100 # 完全加载
tcpConnectTime=10 # TCP建连时间
fristPacketTime=10 # 首包时间=fristPacketTime-serverResponseTime
networkDelay=10 # 网络耗时
requestQuene=10 # 排队耗时
callBackTime=10 # 回调时间

# 首次渲染时间
fristInteractionTime=10 # 首次交互时间
customLoad=10 # 自定义加载
ajaxRequestTime=10 # ajax请求响应时间
sslTime=10
redirectTime=10
domTreatment=10 #dom处理
#HTML加载时间：DNS时间+建连时间+首包时间+剩余包时间
isError=[0,1,2,3]