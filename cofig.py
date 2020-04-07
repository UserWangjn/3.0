#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import ips
import requests
import logging
import sys
import json
import random
import pf

import time
# second.secondding(60-now.second)        #整点发送
ipcount=3
def reate():
    submitdatas = ''
    for i in range(len(pf.redate)):
        submitdatas = submitdatas + pf.redate[i]
        if (i != len(pf.redate) - 1):
            submitdatas = submitdatas + '&'
    # for i in range(10):
    # submitdatas=submitdatas+'&r='+str(random.random()*(time.time( )))
    # submitdatas = submitdatas



logging.basicConfig(level=logging.INFO,stream=sys.stdout)

headerList=["Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 V1_AND_SQ_7.6.3_850_YYB_D QQ/7.6.3.3560 NetType/4G WebP/0.3.0",
            "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN",
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044103 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060737) NetType/4G Language/zh_CN',
            "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.1.2"]

def Submit(url,params,datas,pv_count):
    headers={}
    headers['content-type']='application/json'
    # headers['referrer']="http://192.168.5.71:8080/browser_agent_wailian.html?action=1&key=5"
    headers['referrer']="http://192.168.5.71:8080/browser_agent_wailian_wjn.html?action=1&key=5"
    # headers["Content-Type"]="application/x-www-form-urlencoded"
    # headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'      #设置浏览器
    # headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'#pc
    # headers['User-Agent']='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'#手机
    # headers['User-Agent']="Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN"#微信
    # headers['User-Agent']="Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 V1_AND_SQ_7.6.3_850_YYB_D QQ/7.6.3.3560 NetType/4G WebP/0.3.0"#微信
    # headers['User-Agent']=headerList[random.randint(0,3)]
    headers['User-Agent']=headerList[2]
    # headers["X-Forwarded-For"]=ips.ips[random.randint(0,7)]  #设置ip
    # headers["X-Forwarded-For"]=ips.ips[pv_count]
    # headers["X-Forwarded-For"]=ips.ips[6]
    headers["X-Forwarded-For"]=ips.ips[0] #设置ip
    # print


    Dchost=url+params
    dataB=json.dumps(datas)
    res=requests.post(Dchost,headers=headers,data=dataB)
    # res=requests.get(Dchost,headers=headers)
    # print "data",dataB
    logging.info("reportUser data: url=%s,status=%s"%(res.url,res.status_code))
    print ips.contry[ipcount]
    # print ips.contry[6]
    # print "status_code",type(res.status_code),res.status_code,res.status_code!=200
    print(ips.ip[ipcount])
    # print(ips.ip[6])
    # print "ppv_countv_count",
    def mintes(pv_count):
        return pv_count
    return res.status_code
# if __name__=="__main__":
#     Submit("http://beaconalpha1.tingyun.com/pf?","R8rZlPMX5zQ")
#     Submit("http://192.168.1.100:8080/pf?","R8rZlPMX5zQ")

#3.0地址
# "192.168.1.100:8080"

def Submit1(url,params,pv_count,datas):
    headers={}
    headers['content-type']='application/json'
    # headers['Referer']='http://fdggh.ghj/testSDTY/test/test.jsp'
    # headers["Content-Type"]="application/x-www-form-urlencoded"
    # headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'      #设置浏览器
    # headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'#pc
    # headers['User-Agent']='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'#手机
    # headers['User-Agent']="Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN"#微信
    # headers['User-Agent']="Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 V1_AND_SQ_7.6.3_850_YYB_D QQ/7.6.3.3560 NetType/4G WebP/0.3.0"#微信
    headers['User-Agent']=headerList[random.randint(0,3)]
    headers["X-Forwarded-For"]=ips.ip[pv_count]  #设置ip
    print "ip",headers["X-Forwarded-For"],ips.region[pv_count]

    Dchost=url+params
    dataB=json.dumps(datas)
    res=requests.post(Dchost,headers=headers,data=dataB)
    logging.info("reportUser data: url=%s,status=%s"%(res.url,res.status_code))