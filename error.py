#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pf
import pub

edatas = {}
edatas["pvid"] = pub.pvid
edatas["ref"] = pub.ref
# edatas["referrer"]=pf.datas["referrer"]
edatas["key"] = pub.key
edatas["v"] = pub.v
edatas["av"] = pub.av
edatas["did"] = pub.did
edatas["sid"] = pub.sid
edatas["fu"] = 0
edatas["os"] = 9
edatas["r"] = pub.r

list = []
for key, values in edatas.items():
    list.append(key)

redate = []
for i in range(len(edatas)):
    redate.append(list[i] + '=' + str((edatas.get(list[i]))))

submitdatas = ''
for i in range(len(redate)):
    submitdatas = submitdatas + redate[i]
    if (i != len(redate) - 1):
        submitdatas = submitdatas + '&'

# print submitdatas

errdatas = {"datas":
                [{"o": pub.TS(), "e": "Uncaught TypeError: $.eget is not a function",
                  "l": 32, "c": 11, "r": "http://www.test.com/JSP/test/hi.jsp", "ec": 1,
                  "s": "TypeError: $.eget is not a function\n "
                       "at HTMLButtonElement.<anonymous> "
                       "(file:///C:/Users/YIMAO/Desktop/browser3.0/agent3/page.html:32:11)\n"
                       " at HTMLButtonElement.dispatch (http://cdn.bootcss.com/jquery/1.12.4/jquery.min.js:3:12444)\n"
                       " at HTMLButtonElement.r.handle (http://cdn.bootcss.com/jquery/1.12.4/jquery.min.js:3:9173)",
                  "ep": 0}]}
