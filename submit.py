#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# import thread
import cofig
import pf
import xhr
import time
import datetime
import second
import random
# import spe
import Tr
import error
pagelow=0.5
oprtUse=1
erate=0.5
min_count=10
pv_count=20
oprtcount=0.5
spvr=0
user=1
 #每分钟count
now = datetime.datetime.now()
# t=time.time()
# print now
# print int(round(t*1000))
localtime = time.asctime(time.localtime(time.time()))
# print "本地时间为 :", localtime
# print(60-now.second)
# second.secondding(60-now.second)
# url="http://10.128.2.36:8588/pf?"
# url1="http://10.128.2.36:8588/"
url="http://10.128.2.45:8588/pf?"
url1="http://10.128.2.45:8588/"
# url="http://212.129.130.130:8088/pf?"       #beta
# url1="http://212.129.130.130:8088/"
# url="http://10.129.2.6:8588/pf?"       #demo
# url1="http://10.129.2.6:8588/"
# url="http://dev.syh.tingyun.com:8080/pf?"       #内网
# url1="http://dev.syh.tingyun.com:8080/"
# url="http://10.128.2.24:8588/pf?"         #集成环境
# url1="http://10.128.2.24:8588/"


# url="http://10.128.1.64:8588/pf?"
# url1="http://10.128.1.64:8588/"
# def myThread(threadName,delay):
user=["xiesna","lily","test","lean",'kk','cc','mm','uu','jj','gg']
# user=["xiesna","lily"]
for m in range(min_count):
        t1 = time.time()
        t2 = int(t1*1000)
        t3 = t2 + 100
        localtime1 = time.asctime(time.localtime(time.time()))
        print "本地时间为 :", localtime1
        # pv_count=random.randrange(120,240,2)
        # if m>1:
        #     pv_count=6
        # elif m>2:
        #     pv_count=6
        # for i in range(pv_count):
        for i in range(len(user)):
            # if m>2:
            #     erate=0.2
            # print"第一个i：",i

            # print data[0]
            # second.secondding(5)
            # pf.submitdatass(i,oprtcount)
            ##qz注释以下
            # print "pf……",i
            # time.sleep(delay)
            # cofig.Submit(url,pf.submitdatass(i,oprtcount,min_count,m,spvr,pv_count),pf.dataB,i) #pf
            if i%2==0:
                a='http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian_wjn1966.html'    #操作
    #     datas['ref']="https%3A%2F%2F192.168.5.72%3A8080%2Foprt.com"
    #

                cofig.Submit(url,pf.submitdatass(i,oprtcount,min_count,m,spvr,pv_count,user,a),pf.data(i),i) #pf
                print 'url>>>>%s' %url
                print 'params>>>>%s' %pf.submitdatass(i,oprtcount,min_count,m,spvr,pv_count,user,a)
                print 'datas>>>>%s' %pf.data(i)
            else:
                b='http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian_wjn1967.html'
                cofig.Submit(url,pf.submitdatass(i,oprtcount,min_count,m,spvr,pv_count,user,b),pf.data1(i),i)



            # cofig.Submit(url,pf.submitdatass(i,oprtcount,min_count,m,spvr,pv_count),pf.data(i),i)
            # thread.start_new_thread( print_time, ("Thread-1", 2, ) )
            # thread.start_new_thread( print_time, ("Thread-2", 4, ) )
            ##qz注释以上
            ##qz注释以上
            # cofig.Submit1("http://10.128.1.42:8080/pf?",pf.submitdatas)         #pf
            # cofig.Submit1("http://192.168.1.100:8080/pf?",pf.submitdatas,m)
            # time.sleep(5)


            #qz
            # if (i % 2) == 0:
            #     print ('操作成功……%d')%(i)

            # xhr1=url1+'xhr1?'
            # if i%2==0:
            #     cofig.Submit(xhr1,xhr.submitdatas,xhr.xhr(t2,t3),i)
            # else:
            #     cofig.Submit(xhr1,xhr.submitdatas,xhr.xhr3(t2,t3),i)
            # else:
            #     print('操作失败……%d')%(i)
            #     cofig.Submit("http://10.128.1.42:8080/xhr1?",xhr.submitdatas,xhr.XHR_ITEM2,i)

            #qz

            # cofig.Submit("http://192.168.1.100:8080/xhr1?",xhr.submitdatas,xhr.XHR_ITEM2,i)

            # time.sleep(5)
            # cofig.Submit("http://10.128.1.42:8080/xhr1?",xhr.submitdatas,xhr.XHR_ITEM,m)
            # time.sleep(5)
            # cofig.Submit("http://10.128.1.42:8080/xhr1?",xhr.submitdatas,xhr.XHR_ITEM1,m)
            # time.sleep(5)
            # cofig.Submit("http://10.128.1.42:8080/xhr1?",xhr.submitdatas,xhr.XHR_ITEM2,m)


            # qz一下
                # qz注释以上
            # # # time.sleep(5)#trace
            # time.sleep(5)
            # # print("error次数……%d")%(int(erate*pv_count))
            # for i in range(int(erate*pv_count)):
            #     # time.sleep(1)
            #     cofig.Submit("http://10.128.1.42:8080/err1?",error.submitdatas,error.errdatas,i)  #error
            #     print("error次数……%d")%(i)
            # if (i<int(erate*pv_count)):
            #     err1=url1+'err1?'
            #     cofig.Submit(err1,error.submitdatas,error.errdatas,i)  #error
        # def mintes(m):
        #     return m
        now = datetime.datetime.now()
        second.secondding(60-now.second)




#
# thread1.start()
# thread2.start()
