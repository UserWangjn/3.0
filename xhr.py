#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YIMAO'
import random
import time
import pub
import time

Dc = "http://beaconalpha1.tingyun.com/"
# Dc="http://beaconbeta.tingyun.com/"
# token = "R8rZlPMX5zQ"
# token = "KnYrkt22IcM"
token = pub.key
# token="ciKa736lmuo"

Xdata = {}
Xdata["av"] = pub.av
Xdata["v"] = pub.v
Xdata["key"] = token
Xdata["ref"] = pub.ref
Xdata["referrer"] ="http%3A%2F%2F192.168.3.21%2Fbrowserjs%2F0514%2Fbizid-body.html"
Xdata["pvid"] = pub.pvid
Xdata["did"] = "c90c235e-8661-4891-a274-173ef9b3a515"
Xdata["sid"] = "d5ab7213-f2f5-49b9-8660-a434fc01f156"
Xdata["n"] = "WebAction%2FSpringController%252Fbrowser%252F%7BbrowserAppId%7D%2Fgeneralview"
Xdata["r"] = pub.r

list = []
for key, values in Xdata.items():
    list.append(key)
# print(list)
redate = []
# redate.append('pf?')
for i in range(len(Xdata)):
    redate.append(list[i] + '=' + str((Xdata.get(list[i]))))



# 字符串组合
submitdatas = ''
for i in range(len(redate)):
    submitdatas = submitdatas + redate[i]
    if (i != len(redate) - 1):
        submitdatas = submitdatas + '&'
print submitdatas
statserror=[1,2,3,4,5,]
status=statserror[random.randint(0,4)]+500



print status
t = time.time()
t = int(t*1000)
to = t + 100
XHR_ITEM = {"xhr": [{"req": "post http://192.168.5.50:8081/index.json", "du": "3000",
                      "cb": "500", "status": 200, "err": "0", "rec": "1000", "send": "50",
                      "s_id": "i1FUBB_ygv8#TRuXNhCsBrA", "s_tname": "Transaction/URI/name", "s_tid": 522, "s_rid": 1, "s_duration": 50,
                      "s_user": 100,"s_bid": "",
                      "s_ber": "", "biz_id": "223", "opt_param": {"Xkey": "3", "Xkey1": "2"}
                      }]}
def xhr(t2,t3):
    XHR_ITEM1 = {"xhr": [{"req": "GET http://http://192.168.5.71:8080/aa/index.json1", "du": "3000",
                      "cb": "500", "status": 200, "err": "0", "rec": "1000", "send": "50",
                      "s_id": "i1FUBB_ygv8#TRuXNhCsBrA",  "s_tname": "Transaction/URI/name", "s_tid": 522, "s_rid": 1, "s_duration": 500,
                      "s_user": 'xiesna',"s_bid": "",'start':t2,'end':t3,
                      "s_ber": "", "bizId_param": {"b":"400"}, "opt_param": {"a": "3", "b": "400","m":"5","c":"2"},
                      "request_param": {"key": "1","status":"5","data[0].name":"5","a":"00","b":"1","c":"234","d":"123",
                                        "e":"145","f":"123456999aaa",'data[0].cname':'2'}
                      }]}
    return XHR_ITEM1
def xhr3(t2,t3):
    XHR_ITEM1 = {"xhr": [{"req": "GET http://http://192.168.5.71:8080/aa/index.json1", "du": "3000",
                      "cb": "500", "status": 200, "err": "0", "rec": "1000", "send": "50",
                      "s_id": "i1FUBB_ygv8#TRuXNhCsBrA",  "s_tname": "Transaction/URI/name", "s_tid": 522, "s_rid": 1, "s_duration": 500,
                      "s_user": 'xiesna',"s_bid": "",'start':t2,'end':t3,
                      "s_ber": "", "bizId_param": {"b":"400"}, "opt_param": {},
                      "request_param": {"key": "1","status":"5","data[0].name":"5","a":"00","b":"1","c":"234","d":"123",
                                        "e":"145","f":"123456999aaa",'data[0].cname':'2'}
                      }]}
    return XHR_ITEM1
XHR_ITEM2 = {"xhr": [{"req": "post http://192.168.5.50:8081/./index.json", "du": "3000",
                      "cb": "500", "status": 500, "err": "0", "rec": "1000", "send": "50",
                      "s_id": "i1FUBB_ygv8#TRuXNhCsBrA", "s_tname": "name", "s_tid": 522, "s_rid": 1, "s_duration": 50,
                      "s_user": 'xiesna',"s_bid": "",'start':t,'end':to,
                      "s_ber": "", "bizId_param": {}, "opt_param": {"Xkey": "2", "Xkey1": "2"},
                      "request_param": {"key": "1","status":"5","data[0].name":"5","a":"00","b":"1","c":"234","d":"123",
                                        "e":"145","f":"123456999aaa",'data[0].cname':'2'}
                      }]}

# XHR_ITEM = {"xhr":[{"id":0,"start":pf.datas['r'],"req": "post http://192.168.5.50:8081/testSDTY/servlet/testServlet", "du": "3500",
#                      "cb": "600", "status": "200", "err": "0", "rec": "1000", "send": "50",
#                      "biz_id":7,"opt_param":{"Xkey":"0","Xkey1":"2"}
#                      }]}

# XHR_ITEM = {"xhr":["POST http://172.16.0.100:8080/testSDTY/servlet/testServlet",3500,600,500,0,1000,50]}
