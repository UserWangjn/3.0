#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pf
import random
import time

Sdata = {}
Sdata["av"] = pf.datas["av"]
Sdata["v"] = pf.datas["v"]
Sdata["key"] = pf.datas["key"]
Sdata["ref"] = pf.datas["ref"]
# Sdata["rand"] =str(random.random()*(time.time( )))
Sdata["pvid"] = pf.datas['pvid']
Sdata["did"] = "c90c235e-8661-4891-a274-173ef9b3a515"
Sdata["sid"] = "d5ab7213-f2f5-49b9-8660-a434fc01f156"
Sdata["n"] = "WebAction%2FSpringController%252FApplicationOverviewController%2FdefaultOverview"


def Isource():
    list = []
    for key, values in Sdata.items():
        list.append(key)
    redate = []
    for i in range(len(Sdata)):
        redate.append(list[i] + '=' + str((Sdata.get(list[i]))))
    return redate


# print Isource()

def Join():
    join = ''
    for i in range(len(Isource())):
        join = join + Isource()[i]
        if i != len(Isource()) - 1:
            join = join + "&"
    # print len(Isource())
    # print "join",join
    return join


SParam = Join() + "&rand=" + str(random.random() * (time.time()))
# print(Sdata)




Sdatas = {"key": '3254e2bc-97a9-4cfd-a53e-0dbc3976fd1b', "duration": 3700,
          "status": 1,  # 状态码(0:失败,1:成功)
          "xhrs": [
              {
               #    "id": 8,
               # "start": 17,
               "req": "GET http://192.168.5.50:8081/testSDTY/servlet/testServlet",  # METHOD_AND_XHR_URL,
               "du": 1000,  # DURATION,
               "cb": 600,  # CALLBACK_TIME,
               "status": "200",  # HTTP_STATUS,
               "err": "0",  # ERROR_CODE,
               "rec": "1000",  # BYTES_RECEIVED,
               "send": "50",  # BYTES_SENT,
               # "s_id": "i1FUBB_ygv8#TRuXNhCsBrA",  # APPLICATION_ID_AND_INSTANCE_ID_SECRET,
                "s_id": "",
               # "s_name": "",  # WEB_ACTION_NAME,
               #  "s_du":200  # APPLICATION_SERVER_TIME,
               # "s_qu": "",  # QUEUE_TIME
               }
          ]}


# Sdatas = {"key": "555233f7-ee67-4270-9001-bdf43ebbc294", "duration": 5002, "status": 1,
#           "xhrs": [{"id": 8, "req": "GET views/page/page_home.html?v=51", "start": 17,
#                     "du": 241, "cb": 0, "status": 200, "err": 0, "rec": 14677, "send": 0}
#   {"id": 9, "req": "GET views/page/page_host.html?v=51",
# "start": 20, "du": 494, "cb": 0, "status": 200, "err": 0, "rec": 21148, "send": 0},
#   {"id": 10, "req": "GET views/page/page_url.html?v=51", "start": 22,
#    "du": 506, "cb": 0, "status": 200, "err": 0, "rec": 28505, "send": 0},
#   {"id": 7, "req": "POST /browserapi/browserapp/selectfilter/page/host.json",
#    "start": 13, "du": 527, "cb": 0, "status": 200, "err": 0, "rec": 1255, "send": 95},
#   {"id": 11,
#    "req": "POST /browserapi/highcharts-chart-data/LATEST/accounts/browser/charts/browser-page-load-time.json",
#    "start": 322, "du": 286, "cb": 0, "status": 200, "err": 0, "rec": 1992, "send": 65},
#   {"id": 12,
#    "req": "POST /browserapi/highcharts-chart-data/LATEST/accounts/browser/charts/browser-page-host-count-highest-top.json",
#    "start": 338, "du": 433, "cb": 0, "status": 200, "err": 0, "rec": 666, "send": 65},
#   {"id": 14,
#    "req": "POST /browserapi/highcharts-chart-data/LATEST/accounts/browser/charts/browser-slowpage-processed-account.json",
#    "start": 361, "du": 467, "cb": 0, "status": 200, "err": 0, "rec": 524, "send": 65},
#   {"id": 15,
#    "req": "POST /browserapi/highcharts-chart-data/LATEST/accounts/browser/charts/browser-app-overview-quantile.json",
#    "start": 368, "du": 497, "cb": 0, "status": 200, "err": 0, "rec": 1784, "send": 78},
#   {"id": 13,
#    "req": "POST /browserapi/highcharts-chart-data/LATEST/accounts/browser/charts/browser-page-host-load-time-top.json",
#    "start": 354, "du": 680, "cb": 0, "status": 200, "err": 0, "rec": 668, "send": 65}
#   ]}

# print len(Sdatas["xhrs"])
def ajaxRav():
    count = 0
    for i in range(len(Sdatas["xhrs"])):
        # print Sdatas["xhrs"][i]["du"]
        count = count + Sdatas["xhrs"][i]["du"]
        print(count / len(Sdatas["xhrs"]))
