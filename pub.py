# -*- coding:utf-8 -*-
# __author__ = 'YIMAO'
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import random
def TS():
        t = time.time()
        r = int(round(t * 1000))
        time.sleep(1)
        return r

pvid=["pvid-000","pvid-001","pvid-002","pvid-003","pvid-004"]
r = str(TS())
av = "1.7.0"
v = "1.7.1"
# key='9Vcj8pO5RBU'         #dev
# key='p35OnrDoP8k'           #2.36
# key='4Nl_NnGbjwY'
# key='p35OnrDoP8k'       # 45环境 alarmx  test-智能 应用
key='mGp6E1AcJ9Q'       # 45环境 wjntest  wjn-alert2 应用
# key='p35OnrDoP8k'       #2.36
pvid=pvid[1]
# ref='https%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian.html111%3Fstatus%3D404%26name%3Dlily%26sex%3Dnv%26orderid%3D1'
# ref='http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian1760.html%3Fa%3D101%3Fb%3D202'
# ref='http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian1761.html'
ref='http%3A%2F%2F192.168.5.71%3A8080%2Fbrowser_agent_wailian_wjn1966.html'
# ref='http%3A%2F%2F192.168.2.39%3A8080%2Fportal%2FsubmitOrder'
# did=['c90c235e-8661-4891-a274-173ef9b3a515','c90c235e-8661-4891-a274-173ef9b3a516','c90c235e-8661-4891-a274-173ef9b3a517']
did=['c90c235e-8661-4891-a274-173ef9b3a515']
# did=did[random.randint(0,2)]
did=did[0]
sid='d5ab7213-f2f5-49b9-8660-a434fc01f156'