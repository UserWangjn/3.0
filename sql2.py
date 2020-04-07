#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import MySQLdb
import time
sqlhost="dev-mysql-conf.tingyun.com"
user="lens"
passworld="nEtop2o10"
db="venus_conf"
port=3306

def data1(sqls):
     dbs=MySQLdb.connect(sqlhost,user,"nEtop2o10",db,port)
     cursor = dbs.cursor()
     cursor.execute(sqls)
     t=str(int(dbs.insert_id()))
     dbs.commit()
     results = cursor.fetchall()
     dbs.close()
     return t

agreement_ids=1760
oprt_types=2    #1:server  ,2、browser
browser_types=2    #1:ajax,2:page
busi_ids='5000'  #所属业务id
names='操作test1'
modes=2       #配置操作模式,1:土著手动,2:智能录屏',
weights=1
application_ids=7574
statuss=1    #应用状态，1:启用,0:禁用,-1:已删除'
ctimes=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# mtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print type(ctime)
# sqls='insert into BN_U_OPRT (agreement_id,oprt_type,browser_type,busi_id,name,mode,weight,application_id,status,ctime,mtime,cuser,muser) ' \
#      'VALUES (agreement_ids,oprt_types,browser_types,busi_ids,names,modes,weights,application_id1,status1,ctime1,ctime1,1,1)'
a=1      #0用户体验   1、业务分析  2apm
i=1       #第几个监控对象
n=1

top_level_parent_id=['11965','11965']   #'监控目标顶级节点ID，如果是Server则保存业务系统ID，browser则保存应用ID，Browser的模块则保存模块ID，业务则保存业务的ID',
parent_id=['0']
# target_id='11794'   #业务系统
target_id=['11965','11820']   #业务系统id
target_name=['test-alarm-learn','test-ajax1']
agreement_id='1998'
alarm_type='1' #1策略告警    2只能告警
alarm_settings_id=['174','173']
policy_id=['217','224']

ts=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

target_type=['1','2','3']    #用户体验   #业务分析   #apm
target_children_type1 = ["BAPP","BM","BHOST","BPG","BAJ","BOP"]  #应用，模块，主机，关键页面，Ajax，关键操作
target_children_type2=["BZ","BZOP"]   #业务，业务操作
target_children_type3=['SBZ','SAPP','TX','EXT','IF']   #业务系统，应用，事务，外部服务，服务接口
target_children_type=[target_children_type1,target_children_type2,target_children_type3]
sqls="INSERT INTO NL_U_ALARM_EVENTS_TRACE (target_type, target_children_type, top_level_parent_id, parent_id, target_id, target_name, agreement_id, status, read_status, alarm_type, alarm_settings_id, policy_id, begin_time,is_useful, message, ignore_status, sample_group, sample_group_values, ctime, mtime) " \
                                        "VALUES ("+target_type[a]+",'"+target_children_type[a][i]+"', '"+top_level_parent_id[n]+"', '"+parent_id[0]+"', '"+target_id[n]+"', '"+target_name[n]+"', '"+agreement_id+"', '1', '0', '"+alarm_type+"', '"+alarm_settings_id[n]+"', '"+policy_id[n]+"', '"+ts+"', '0', '', '0', '1', '', '"+ts+"', '"+ts+"')"
# print "sqls",type(target_children_type3[a])
# print "type",type(target_type[a])


# print "sqls",sqls


sqls="INSERT INTO NL_U_ALARM_EVENTS (event_trace_id, related_event_id, event_type, event_level, status, begin_time, ctime) " \
"VALUES ('"+data1(sqls)+"', '0', '1', '1', '1','"+ts+"','"+ts+"')"


metric_Aapplication=['au','su','eu','eau','rast','rrt','rht','oa','ort','dns','jer','spvr','qps']   #应用指标/模块/主机
metric_bvapplication=['oa','oec','soc']#应用vip
metric_bgjoprt=['oa','ort','oc','oec','soc']   #关键操作
metric_bgjpage=['fst','fpt','drt','pd','rast','rrt','rht','oa','ort','dns','jer','tcp','fp','spvr','qps','spv']#关键页面
metric3=[]
warn_rate=[1,2,3]
Cril_rate=[5,6,7]
t=data1(sqls)
for i in range(3):
     sqls="INSERT INTO NL_U_ALARM_EVENTS_DETAIL (event_id, metric_id, threshold, value, request_count, compare_type, threshold_type, ctime) " \
      "VALUES ('"+t+"', '"+metric_bvapplication[0]+"', '2', '10', '100', '1', '1', '"+ts+"')"


data1(sqls)