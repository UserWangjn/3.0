#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from pykafka import KafkaClient
#from kafka import KafkaProducer

import json
import logging
import time
import sys
import requests
import json
import time
# from kafka import KafkaProducer

def kafka():
    t = time.time()
    t = int(t*1000)
    to = t + 500
    # print type(to)
    client = KafkaClient(hosts = "10.128.2.40:9092" )
    topic = client.topics['ty-brs-access-log']
    producer = topic.get_producer()
    producer.start()
    count=9
    sessionkey='4Nl_NnGbjwY'
    fst=2
    spvr=0.1
    errorate=0.2

    oprtused=0.7
    # times="25/Sep/2018:04:03:00"
    for m in range(count):
        localtime1 = time.asctime(time.localtime(time.time()))
        print "本地时间为 :", localtime1
        times1="29/Nov/2019:13:0"+str(m)+":00"
        # times1="22/Nov/2019:15:57:00"
        # dt = "2018-10-19 17:01:00"
        # dt1 = "2018-10-19 17:01:30"
        #转换成时间数组
        # timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
        # timeArray1 = time.strptime(dt1, "%Y-%m-%d %H:%M:%S")
        # #转换成时间戳
        # timestamp = int(time.mktime(timeArray))*1000
        # timestamp1 = int(time.mktime(timeArray1))*1000
        # print timeArray,timeArray1,timestamp,timestamp1


        # times2="20/Sep/2018:04:13:30"
        # producer.produce('192.168.5.71	24/Jul/2018:10:40:49 +0800	/pf?v=1.6.1&ee=10&sw=1024&av=1.7.0&ce=2&s_id=i1FUBB_ygv8%23TRuXNhCsBrA&je=0&cs=60&s_ber=400&es=0&ct=100&le=1021&rs=448&tue=0&re=600&r=1531795777000&ls=359&tus=0&sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&s_rid=101&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fp=556&s_duration=119&fs=439&s_bid=201&de=60&s_user=Network&key=4DREB64oG3Q&biz_id=200&fi=150&dr=556&ds=10&a=1&qs=210&oi=360&f=0&did=c90c235e-8661-4891-a274-173ef9b3a515&referrer=http%3A%2F%2F192.168.3.21%2Fbrowserjs%2F0514%2Fbizid-body.html&oe=360&oc=409&s_tid=100&pvid=pvid-001&sh=768&s_tname=fp&sl=200&ue=1&os=310&trflag=1001	37	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.1.2	182.106.204.211	{"opt_param": {"key2": 2, "key1": 1}}	0.000	-')
    # producer.produce('192.168.5.71	23/Jul/2018:11:31:49 +0800	/pf?v=1.6.1&ee=10&sw=1024&av=1.7.0&ce=2&s_id=i1FUBB_ygv8%23TRuXNhCsBrA&je=0&cs=60&s_ber=400&es=0&ct=100&le=446&rs=327&tue=0&re=600&r=1531795777000&ls=359&tus=0&sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&s_rid=101&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fp=456&s_duration=19&fs=639&s_bid=201&de=60&s_user=Network&key=4DREB64oG3Q&biz_id=200&fi=150&dr=856&ds=10&a=1&qs=210&oi=360&f=0&did=c90c235e-8661-4891-a274-173ef9b3a515&referrer=http%3A%2F%2F192.168.3.21%2Fbrowserjs%2F0514%2Fbizid-body.html&oe=360&oc=409&s_tid=100&pvid=pvid-001&sh=768&s_tname=fp&sl=200&ue=1&os=310&trflag=1001	37	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.1.2	182.106.204.211	{"opt_param": {"key2": 2, "key1": 1}}	0.000	-')
    # producer.produce('192.168.5.71	'+times+' +0800	/pf?v=1.6.1&ee=10&sw=1024&av=1.7.0&ce=2&s_id=i1FUBB_ygv8%23TRuXNhCsBrA&je=0&cs=60&s_ber=400&es=0&ct=100&le=546&rs=327&tue=0&re=600&r=1531795777000&ls=359&tus=0&sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&s_rid=101&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fp=600&s_duration=10&fs=50&s_bid=201&de=60&s_user=Network&key='+sessionkey+'&biz_id=200&fi=150&dr=300&ds=10&a=1&qs=210&oi=360&f=0&did=c90c235e-8661-4891-a274-173ef9b3a515&referrer=http%3A%2F%2F192.168.3.21%2Fbrowserjs%2F0514%2Fbizid-body.html&oe=360&oc=409&s_tid=100&pvid=pvid-001&sh=768&s_tname=fp&sl=200&ue=1&os=310&trflag=1001	37	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.1.2	182.106.204.211	{"opt_param": {"key2": 2, "key1": 1}}	0.000	-')
    #     producer.produce('192.168.5.71	'+times1+' +0800	/pf?v=1.6.1&ee=10&sw=1024&av=1.7.0&ce=2&s_id=i1FUBB_ygv8%23TRuXNhCsBrA&je=0&cs=60&s_ber=400&es=0&ct=100&le=546&rs=327&tue=0&re=600&r=1531795777000&ls=359&tus=0&sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&s_rid=101&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fp=200&s_duration=50&fs=100&s_bid=201&de=60&s_user=Network&key='+sessionkey+'&biz_id=200&fi=150&dr=500&ds=10&a=1&qs=210&oi=360&f=0&did=c90c235e-8661-4891-a274-173ef9b3a515&referrer=http%3A%2F%2F192.168.3.21%2Fbrowserjs%2F0514%2Fbizid-body.html&oe=360&oc=409&s_tid=100&pvid=pvid-001&sh=768&s_tname=fp&sl=200&ue=1&os=310&trflag=1001	37	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.1.2	182.106.204.211	{"opt_param": {"key2": 2, "key1": 1}}	0.000	-')
    #     producer.produce('192.168.5.71	'+times1+' +0800	/pf?v=1.7.1&ee=1&sw=1024&av=1.7.0&ce=23&s_id=i1FUBB_ygv8%23TRuXNhCsBrA&je=0&cs=12&s_ber=400&es=0&ct=1&le=440&rs=34&tue=0&re=34&r=1539832425305&ls=34&tus=0&sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&s_rid=101&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fp=100&s_duration=1&fs=113&s_bid=&de=12&s_user=xiesna&key=6C6LVqKv1U8&biz_id=200&fi=1&dr=200&ds=1&a=200&qs=23&oi=35&f=0&did=c90c235e-8661-4891-a274-173ef9b3a515&referrer=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Faction%3D1%26key%3D5&oe=35&oc=35&s_tid=100&pvid=pvid-002&sh=768&s_tname=Transaction%2FURI%2Fportal%2ForderStatus&sl=22&ue=1&os=34&trflag=1001	70	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN	210.212.193.192	{"opt_param": {"key2": 2, "key1": 1}, "bizId_param": {"key": "value"}}	0.000	-')

        # for i in range(count):
        #     if i <spvr*count:
        fp=random.randrange(10,20,2)
        producer.produce('192.168.5.71	'+times1+' +0800	/pf?v=1.6.1&ee=10&sw=1024&av=1.7.0&ce=2&s_id=i1FUBB_ygv8%23TRuXNhCsBrA&je=0&cs=60&s_ber=400&es=0&ct=100&le=546&rs=327&tue=0&re=600&r=1531795777000&ls=359&tus=0&sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&s_rid=101&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fp='+str(fp)+'&s_duration=50&fs='+str(fp)+'&s_bid=201&de=60&s_user=Network&key='+sessionkey+'&biz_id=200&fi=150&dr=100&ds=10&a=1&qs=210&oi=360&f=0&did=c90c235e-8661-4891-a274-173ef9b3a515&referrer=http%3A%2F%2F192.168.3.21%2Fbrowserjs%2F0514%2Fbizid-body.html&oe=360&oc=409&s_tid=100&pvid=pvid-001&sh=768&s_tname=fp&sl=200&ue=1&os=310&trflag=1001	37	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.1.2	182.106.204.211	{"opt_param": {"key2": 2, "key1": 1}}	0.000	-')
        # producer.produce('192.168.5.67 - - ['+times1+' +0800] "POST /pf?v=1.7.1&ee=500&sw=1024&av=1.7.0&ce=21&s_id=i1FUBB_ygv8%23TRuXNhCsBrA&je=0&cs=11&es=0&ct=500&le=40&rs=31&tue=0&re=31&r=1574064967744&ls=40&tus=0&sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&s_rid=101&ns=1574064970841&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian1761.html&fp=500&s_duration=500&fs=10&s_isError=0&s_bid=&de=11&s_user=test&key='+sessionkey+'&biz_id=200&fi=10&dr=10&ds=1&a=10&qs=21&oi=531&f=0&did=c&referrer=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html1111%3Faction%3D1%26key%3D5&oe=531&oc=540&s_tid=100&pvid=pvid-001&sh=768&s_tname=Transaction%2FURI%2Fportal%2ForderStatus&sl=11&ue=1&os=31&trflag=1001 HTTP/1.1" 200 18 "-" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"')
        #     else:
        #         fp=10
        #         print("pf……%d")%(i)
        #         producer.produce('192.168.5.71	'+times1+' +0800	/pf?v=1.6.1&ee=10&sw=1024&av=1.7.0&ce=2&s_id=i1FUBB_ygv8%23TRuXNhCsBrA&je=0&cs=60&s_ber=400&es=0&ct=100&le=546&rs=327&tue=0&re=600&r=1531795777000&ls=359&tus=0&sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&s_rid=101&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fp='+str(fp)+'&s_duration=50&fs=10&s_bid=201&de=60&s_user=Network&key='+sessionkey+'&biz_id=200&fi=150&dr=100&ds=10&a=1&qs=210&oi=360&f=0&did=c90c235e-8661-4891-a274-173ef9b3a515&referrer=http%3A%2F%2F192.168.3.21%2Fbrowserjs%2F0514%2Fbizid-body.html&oe=360&oc=409&s_tid=100&pvid=pvid-001&sh=768&s_tname=fp&sl=200&ue=1&os=310&trflag=1001	37	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.1.2	182.106.204.211	{"opt_param": {"key2": 2, "key1": 1}}	0.000	-')
            #
            # if i<errorate*count:
            #     time.sleep(5)
            #     print("error……%d")%(i)
            #     producer.produce('192.168.5.71	'+times1+' +0800	/err1?sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&did=c90c235e-8661-4891-a274-173ef9b3a515&os=9&v=1.7.1&pvid=pvid-001&r=1539152834071&key='+sessionkey+'&av=1.7.0&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fu=0	497	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN	24.232.0.17	{"datas": [{"c": 11, "r": "http://www.test.com/JSP/test/hi.jsp", "e": "Uncaught TypeError: $.eget is not a function", "ec": 1, "s": "TypeError: $.eget is not a function at HTMLButtonElement.<anonymous> (file:///C:/Users/YIMAO/Desktop/browser3.0/agent3/page.html:32:11) at HTMLButtonElement.dispatch (http://cdn.bootcss.com/jquery/1.12.4/jquery.min.js:3:12444) at HTMLButtonElement.r.handle (http://cdn.bootcss.com/jquery/1.12.4/jquery.min.js:3:9173)", "l": 32, "o": 1539152835072, "ep": 0}]}	0.000	-')

                # producer.produce('192.168.5.71	'+times1+' +0800	/err1?sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&did=c90c235e-8661-4891-a274-173ef9b3a515&os=9&v=1.7.1&pvid=pvid-001&r=1538291639770&key='+sessionkey+'&av=1.7.0&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fu=0	497	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN	24.232.0.17	{"datas": [{"c": 11, "r": "http://www.test.com/JSP/test/hi.jsp", "e": "Uncaught TypeError: $.eget is not a function", "ec": 1, "s": "TypeError: $.eget is not a function at HTMLButtonElement.<anonymous> (file:///C:/Users/YIMAO/Desktop/browser3.0/agent3/page.html:32:11) at HTMLButtonElement.dispatch (http://cdn.bootcss.com/jquery/1.12.4/jquery.min.js:3:12444) at HTMLButtonElement.r.handle (http://cdn.bootcss.com/jquery/1.12.4/jquery.min.js:3:9173)", "l": 32, "o": 1538291640771, "ep": 0}]}	0.000	-')
        # time.sleep(5)
        # producer.produce('192.168.5.71	'+times1+' +0800	/err1?sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&did=c90c235e-8661-4891-a274-173ef9b3a515&os=9&v=1.7.1&pvid=pvid-002&r=1538291639770&key='+sessionkey+'&av=1.7.0&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fu=0	497	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN	24.232.0.17	{"datas": [{"c": 11, "r": "http://www.test.com/JSP/test/hi.jsp", "e": "Uncaught TypeError: $.eget is not a function", "ec": 1, "s": "TypeError: $.eget is not a function at HTMLButtonElement.<anonymous> (file:///C:/Users/YIMAO/Desktop/browser3.0/agent3/page.html:32:11) at HTMLButtonElement.dispatch (http://cdn.bootcss.com/jquery/1.12.4/jquery.min.js:3:12444) at HTMLButtonElement.r.handle (http://cdn.bootcss.com/jquery/1.12.4/jquery.min.js:3:9173)", "l": 32, "o": 1538291640771, "ep": 0}]}	0.000	-')

        # producer.produce("192.168.5.71\t"+times1+" +0800\t/xhr1?pvid=f87b29e3-60f4-4665-a2b8-bb6176092499&ref=http%3A%2F%2Fwww.learn.com%3A63342%2Fbrowser3test%2Fmodule%2Findex.html%3F_ijt%3Dv3aoanhaqbpfdtco6bk2mmqma4&referrer=&key="+sessionkey+"&v=3.0.2&av=3.0.2&did=b5878694-9e1c-4bbb-bc90-db47dd8efa62&sid=42d0d6a9-a5a2-4b25-8587-64a80bce8ca7&__r=1534154046994\t498\t000\thttp://localhost:63342/browser3test/module/index.html?_ijt=v3aoanhaqbpfdtco6bk2mmqma4\tMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36\t182.106.204.211\t{\"xhr\":[{\"id\":1,\"req\":\"POST http://192.168.5.50:8081/./index.json\",\"start\":1539771300000,\"end\":1539771303000,\"du\":48,\"cb\":0,\"status\":200,\"err\":0,\"rec\":93,\"send\":34,\"biz_id\":\"\",\"opt_param\":{},\"request_param\":{\"data#overview.max\":1000},\"s_id\":\"LMyJ2xMkn50#vVLPd0x06rw\",\"s_tname\":\"WebAction/URI%2Fmobilepromotion%2Fgiftbagsecond%2Findex/\",\"s_tid\":\"87edab502aff4a88\",\"s_rid\":\"fa8536a7-fbb2-48c0-ae59-9bbd378e12ed\",\"s_duration\":69,\"s_user\":\"fa8536a7-fbb2-48c0-ae59-9bbd378e12ee\",\"s_bid\":\"11111\",\"s_ber\":\"11111\"}]}\t0.001\t-")
        # print("oprtused……%d")%(oprtused*count)
        # if m <oprtused*count:

        #     producer.produce('192.168.5.71	'+times1+' +0800	/xhr1?sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&did=c90c235e-8661-4891-a274-173ef9b3a515&referrer=http%3A%2F%2F192.168.3.21%2Fbrowserjs%2F0514%2Fbizid-body.html&av=1.7.0&n=WebAction%2FSpringController%252Fbrowser%252F%7BbrowserAppId%7D%2Fgeneralview&pvid=pvid-001&r=1539832425305&key=6C6LVqKv1U8&v=1.7.1&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1	565	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN	210.212.193.192	{"xhr": [{"status": 500, "s_duration": 50, "opt_param": {"Xkey": "2", "Xkey1": "2"}, "end": '+str(timestamp)+', "bizId_param": {}, "err": "0", "s_user": "xiesna", "s_ber": "", "cb": "500", "s_bid": "", "req": "post http://192.168.5.50:8081/./index.json", "request_param": {"status": "5", "a": "00", "c": "234", "b": "1", "e": "145", "d": "123", "key": "1", "f": "123456999aaa", "data[0].name": "5", "data[0].cname": "2"}, "send": "50", "s_tid": 522, "s_id": "i1FUBB_ygv8#TRuXNhCsBrA", "s_tname": "name", "rec": "1000", "s_rid": 1, "du": "3000", "start": '+str(timestamp)+'}]}	0.000	-')
        # time.sleep(6000)
    producer.stop()

    print "等待……"
kafka()
def baseline():
    headers={}
    headers['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
    headers['X-Requested-With']='XMLHttpRequest'
    url="http://192.168.1.100:8082/testTime"
    data={"targetType":"BAPP",
      "targetCategory": "app_id=7847",
      "targetName": "7847",
      "metricName": "spvr",
      "startTime": "2018-09-25 03:00:00",
      "endTime": "2018-09-25 04:00:00",
      "needVar": "true"}
    # datas=json.dumps(data)
    # r=requests.post(url,headers=headers,data=datas)
    url1='http://192.168.1.100:8082/testTime'
    r=requests.get(url1,params='%7B%0A++++++%22targetType%22%3A+%22BAPP%22%2C%0A++++++%22targetCategory%22%3A+%22app_id%3D7847%22%2C%0A++++++%22targetName%22%3A+%227847%22%2C%0A++++++%22metricName%22%3A+%22spvr%22%2C%0A++++++%22startTime%22%3A+%222018-09-25+04%3A00%3A00%22%2C%0A++++++%22endTime%22%3A+%222018-09-25+05%3A00%3A00%22%2C%0A++++++%22needVar%22%3A+%22true%22%0A++++%7D',headers=headers)
    print 'error……',r.text,r.status_code


# baseline()





# client = KafkaClient(hosts = "10.128.2.39:9092" )
#
# topic = client.topics['ty-brs-access-log']
#
#
# producer = topic.get_producer()
# producer.start()
# times1="18/Nov/2019:15:0"+str(m)+":00"
#   # 生产消息
msg_dict = {
    "sleep_time": 10,
    "db_config" : {
      "database"  : "ty-brs-access-log",
      "host"      : "10.128.2.39",
      "user"      : "tingyun",
      "password"  : "nEtben@2_19"
    },
    "table"     : "msg",
    "msg"       : '192.168.5.71	'+times1+' +0800	/pf?v=1.6.1&ee=10&sw=1024&av=1.7.0&ce=2&s_id=i1FUBB_ygv8%23TRuXNhCsBrA&je=0&cs=60&s_ber=400&es=0&ct=100&le=546&rs=327&tue=0&re=600&r=1531795777000&ls=359&tus=0&sid=d5ab7213-f2f5-49b9-8660-a434fc01f156&s_rid=101&ref=http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1&fp='+str(fp)+'&s_duration=50&fs=10&s_bid=201&de=60&s_user=Network&key='+sessionkey+'&biz_id=200&fi=150&dr=100&ds=10&a=1&qs=210&oi=360&f=0&did=c90c235e-8661-4891-a274-173ef9b3a515&referrer=http%3A%2F%2F192.168.3.21%2Fbrowserjs%2F0514%2Fbizid-body.html&oe=360&oc=409&s_tid=100&pvid=pvid-001&sh=768&s_tname=fp&sl=200&ue=1&os=310&trflag=1001	37	000	-	Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.1.2	182.106.204.211	{"opt_param": {"key2": 2, "key1": 1}}	0.000	-'
  }
# msg = json.dumps(msg_dict)
# producer.produce(msg)
# producer.stop()










