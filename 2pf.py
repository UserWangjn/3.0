#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import cofig
import pf
import xhr
import time
import datetime
import second
import spe
import Tr
import error

erate=0.2
min_count=1
pv_count=20  #每分钟count
now = datetime.datetime.now()
# t=time.time()
# print now
# print int(round(t*1000))
localtime = time.asctime(time.localtime(time.time()))
# print "本地时间为 :", localtime
# print(60-now.second)
# second.secondding(60-now.second)
# Dchost="http://beaconalpha1.tingyun.com"   #内网
# Dchost="http://beaconbeta.tingyun.com"   #beta
Dchost="http://beacon.tingyun.com"

for m in range(min_count):
    localtime1 = time.asctime(time.localtime(time.time()))
    print "本地时间为 :", localtime1
    for i in range(pv_count):
          # second.secondding(10)
          cofig.Submit(Dchost+"/pf?",pf.submitdatas,pf.dataB,m)         #pf
          # cofig.Submit(Dchost+"/pf?",pf.submitdatas,pf.dataB,m)
          # cofig.Submit(Dchost+"/xhr1?",xhr.submitdatas,xhr.XHR_ITEM,m)  #xhr
          # time.sleep(2)
          # cofig.Submit(Dchost+"/spe?",spe.SParam,spe.Sdatas,m)  #spe
          # cofig.Submit1(Dchost+"/pf?",pf.submitdatas,i,Tr.TrDate)        #?
          # time.sleep(2)
          # if i<pv_count*erate:
             # cofig.Submit("http://beaconalpha1.tingyun.com/err1?",error.submitdatas,error.errdatas,m)
            # cofig.Submit(Dchost+"/err1?",error.submitdatas,error.errdatas,m)

    #3.0
          # second.secondding(10)
          # cofig.Submit("http://192.168.1.100:8080/pf?",pf.submitdatas,pf.dataB,m)         #pf
        # cofig.Submit1("http://192.168.1.100:8080/pf?",pf.submitdatas,m)
        # cofig.Submit("http://192.168.1.100:8080/xhr1?",xhr.submitdatas,xhr.XHR_ITEM,m)  #xhr
        # time.sleep(25)
        # cofig.Submit("http://192.168.1.100:8080/xhr1?",xhr.submitdatas,xhr.XHR_ITEM1,pv_count)
        # time.sleep(5)
        # cofig.Submit("http://192.168.1.100:8080/xhr1?",xhr.submitdatas,xhr.XHR_ITEM,m)
    #     cofig.Submit("http://192.168.1.100:8080/err1?",error.submitdatas,error.errdatas,pv_count)    #error
    #     cofig.Submit("http://192.168.1.100:8080/pf?",pf.submitdatas,Tr.TrDate,i)    #trace
          def mintes(m):
            return m
    now = datetime.datetime.now()
    second.secondding(60-now.second)


    # second.secondding(60)

