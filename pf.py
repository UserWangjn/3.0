#!/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'YIMAO'

import random
import time
import pfdate_set
import json
import requests
import cofig
import pf
import pub
def submitdatass(i,oprtcount,min_count,m,spvr,pv_count,user,c):
    # if i<spvr*pv_count:
    # if i%2==0:
    #
    #     fs=801
    # else:
    #     fs=113
    # fs=random.randrange(550,700,2)
    # fs=random.randrange(300,400,2)
    # fp=random.randrange(300,400,2)
    tcpConnectTime=random.randrange(10000,11000,2)
    fs=3700    # 首屏
    fp=3800    # 白屏
    # # print ("fs……%d")%(fs)
    # # fs=113
    # if i<3:
    #     fp=6000
    # else:
    #     fp=5000
    # print ("spv……%d,fs……%d")%(spvr*pv_count,fs)

    # print m
    # if m>3:
    #     pfdate_set.fristPacketTime=1000
    # else:
    #     pfdate_set.fristPacketTime=600
    # print("首包……:%d")%(pfdate_set.fristPacketTime)

    def TS():
        t = time.time()
        r = int(round(t * 1000))
        time.sleep(1)
        return r



    ip = "119.75.213.61"
    datas = {}
    datas['f'] = 0
    datas['a'] = pfdate_set.serverResponseTime  # 服务端响应时间
    datas['ds'] = datas['f'] + pfdate_set.cachetime
    datas['de'] = datas['ds'] + pfdate_set.dnsTime
    datas['cs'] = datas['de']
    # datas['ce'] = datas['cs'] + pfdate_set.tcpConnectTime
    datas['ce'] = datas['cs'] + tcpConnectTime
    # datas['ce'] = datas['cs'] + a
    datas['sl'] = datas['ce'] - pfdate_set.sslTime
    datas['es'] = 0
    datas['ee'] = datas['es'] + pfdate_set.redirectTime
    datas['qs'] = datas['ce']
    datas['rs'] = datas['qs'] + pfdate_set.fristPacketTime
    datas['re'] = datas['qs'] + pfdate_set.fristPacketTime
    datas['os'] = datas['re']
    datas['oe'] = datas['os'] + pfdate_set.domTreatment
    datas['oi'] = datas['os'] + pfdate_set.domTreatment
    datas['oc'] = datas['oe'] + pfdate_set.pagePrint
    datas['ls'] = datas['re'] + pfdate_set.pagePrint
    # datas['le'] = datas['re'] + pfdate_set.pagePrint+119640  # 完全加载
    datas['le'] = datas['re'] + pfdate_set.pagePrint # 完全加载
    datas['ue'] = 1
    datas['fi'] = pfdate_set.fristInteractionTime
    datas['fp'] = fp  # 白屏
    datas['dr'] = pfdate_set.domRedayTime  # 可交互
    datas['fs'] =fs  # 首屏
    datas['ct'] = pfdate_set.customLoad
    # datas['je']=pfdate_set.jsErrorRate*100
    datas['je'] = 0
    datas['sh'] = 768
    datas['sw'] = 1024
    datas['tus'] = 0
    datas['tue'] = 0
    datas['r'] = pub.r
    datas['av'] = pub.av
    datas['v'] = pub.v
    datas['ns']=TS()
    # datas['ns']=int(round(time.time() * 1000))


    # datas['key'] = "i1rDl-QLzLY"  # 3.0
    # datas['key'] = "qeO7kZ-bSJk"  # 3.0
    # datas['key'] = "SOaSXXTHWVE"  #test_trace

    datas['key']=pub.key
    # datas['key']="RvM3_SkYtrQ"   #beta
    # datas['ref'] = "http%253a%252f%252f192.168.5.19%253a8890%2Fjd.com"
    # datas['ref'] = "http%253a%252f%252f192.168.5.20%253a8880%2Fwww.baidu.com"
    # datas['ref'] = "http%3A%2F%2F192.168.5.71%3A8080%2F11111111wailian.cn%3Faction%3D1%26key%3D5"
    datas['ref'] = c
    # datas['ref'] = "https%3A%2F%2Fwww.baidu.cn"
    # datas['ref'] = "http%3A%2F%2F192.168.5.71%3A8080%2F1_agent_wailian.com%3Faction%3D1%26key%3D5"
    # datas['referrer'] = "http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html1111%3Faction%3D1%26key%3D5"
    datas['referrer'] = "http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian_wjn.html1111%3Faction%3D1%26key%3D5"
    # datas['ref'] = "http://192.168.5.19:8890/www.baidu.com"
    datas["did"] = pub.did[random.randint(0,2)]
    datas["sid"] = pub.sid
    datas["trflag"] = "1001"
    # datas["id"]="i1FUBB_ygv8%23TRuXNhCsBrA"
    # datas["id"]="i1FUBB_ygv8%23TRuXNhCsBrA"
    # pvid=["pvid-000","pvid-001","pvid-002","pvid-003","pvid-004"]
    datas['pvid'] = pub.pvid
    # # 新增
    datas['biz_id'] = "200"
    datas["s_id"]="i1FUBB_ygv8%23TRuXNhCsBrA"
    # datas["s_id"]=""
    datas["s_tname"] = "Transaction%2FURI%2Fportal%2ForderStatus"
    datas["s_tid"] = 100
    datas["s_rid"] = 101
    datas["s_duration"] = 2000       #服务端响应时间
    # user=["Network"]

    # user=["xiesna","lily","test","lean",'kk','cc','mm','uu','jj','gg']
    if i <len(user):
        datas["s_user"] = user[i]
    # datas["s_user"] = user[random.randrange(0,5)]
    # datas["s_user"] = 'xiesna'
        print "user……",datas["s_user"]

    datas["s_bid"] = ""
    # datas["s_ber"] = "400"
    datas["s_isError"] = pfdate_set.isError[0]




    # datas="{\"request_param\": {\"action\": \"4123\",\"key\":\"9\"}}"


# dataB = {'opt_param': {}}

# dataB=json.dumps(dataB)
# subdata=["pf?",datas]
# print "subdata",subdata

# datas['biz_id']

    # print ("第n次……%d;操作次数%d")%(i,oprtcount)
    # print(i <=oprtcount)
    # if i%2==0:
    #     datas['ref']='http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian1762.html'    #操作
    # #     datas['ref']="https%3A%2F%2F192.168.5.72%3A8080%2Foprt.com"
    # #
    # else:
    #     datas['ref']='http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian1761.html'
    # datas['ref']='http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html111%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1'
    # datas['ref']='http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian1760.html%3Fa%3D101%3Fb%3D202'

    # print(datas['ref'])
    list = []
    for key, values in datas.items():
        list.append(key)
    # print(list)
    redate = []
    # redate.append('pf?')
    for i in range(len(datas)):
        redate.append(list[i] + '=' + str((datas.get(list[i]))))
    # 字符串组合
    submitdatas = ''
    for i in range(len(redate)):
        submitdatas = submitdatas + redate[i]
        if (i != len(redate) - 1):
            submitdatas = submitdatas + '&'
    # for i in range(10):
    # submitdatas=submitdatas+'&r='+str(random.random()*(time.time( )))
    submitdatas = submitdatas
    return submitdatas
# print redate
# print list
#     dns = datas["de"] - datas["ds"]
#     print "dns耗时", dns
#     tcp=0
#     ssl=0
#     if datas["sl"] > 0:
#         ssl=datas["ce"] - datas["sl"]
#         # print "ssl", datas["ce"] - datas["sl"]
#         tcp=datas["sl"] - datas["cs"]
#         # print "tcp", datas["sl"] - datas["cs"]
#     elif datas["sl"] == 0:
#         ssl=0
#         # print "ssl", 0
#         tcp=datas["ce"] - datas["cs"]
#         # print "tcp", datas["ce"] - datas["cs"]
#     tcp=tcp
#     ssl=ssl
#     request_time=datas["rs"] - datas["ce"]
#     # print "request_time", datas["rs"] - datas["ce"]
#     response_time=datas["re"] - datas["rs"]
#     # print "response_time", datas["re"] - datas["rs"]
#     # print "cache缓存", datas["re"] - dns-tcp-ssl-request_time-response_time
#     # print "可交互",datas["dr"]
#     le=0
#     if datas["le"]>0:
#         return # print "页面加载",datas["le"]
#     elif datas["le"]==0:
#         return # print "页面加载",datas["ue"]
# dataB={'opt_param':{"c":1,"b":""},"bizId_param": {
#             "a": "1"}}
# dataB={'opt_param':{"mce":"100"},"bizId_param": {"b":"200"}}
# dataC={'opt_param':{},"bizId_param": {"b":"400"}}
def data(i):
    dataB={'opt_param':{"mce":"100"},"bizId_param": {"b":str(i)}}
    # dataC={'opt_param':{"mce":"100"},"bizId_param": {"b":"400"}}
    return dataB

def data1(i):
    datac={'opt_param':{"mce":"100"},"bizId_param": {"b":str(i)}}
    # dataC={'opt_param':{"mce":"100"},"bizId_param": {"b":"400"}}
    return datac