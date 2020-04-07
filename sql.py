#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import MySQLdb
import time
import sys
# import os.path

# print "……",os.path.exists(time)

reload(sys)
sys.setdefaultencoding('utf-8')
# sys.setdefaultencoding('utf8')
sqlhost="10.128.2.39"       #beta
user="lens"
passworld="nEtop2_18"

# sqlhost="dev-mysql-conf.tingyun.com"
# user="lens"
# passworld="nEtop2o10"
db="venus_conf"
port=3306

def data1(sqls):
     dbs=MySQLdb.connect(sqlhost,user,passworld,db,port)
     cursor = dbs.cursor()
     cursor.execute(sqls)
     t=str(int(dbs.insert_id()))
     dbs.commit()
     results = cursor.fetchall()
     print results
     dbs.close()
     return t

data1(sqls="select * from ACE_APPLICATION limit 1")

# agreement_ids=1760
# oprt_types=2    #1:server  ,2、browser
# browser_types=2    #1:ajax,2:page
# busi_ids='5000'  #所属业务id
# names='操作test1'
# modes=2       #配置操作模式,1:土著手动,2:智能录屏',
# weights=1
# application_ids=7574
# statuss=1    #应用状态，1:启用,0:禁用,-1:已删除'
# ctimes=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# # mtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# # print type(ctime)
# # sqls='insert into BN_U_OPRT (agreement_id,oprt_type,browser_type,busi_id,name,mode,weight,application_id,status,ctime,mtime,cuser,muser) ' \
# #      'VALUES (agreement_ids,oprt_types,browser_types,busi_ids,names,modes,weights,application_id1,status1,ctime1,ctime1,1,1)'
# a=3       #0用户体验   1、业务分析  2apm  4小程序
# i=0     #第几个监控对象
# n=3
# top_level_parent_id=['7839','7804','7820','3']  #'监控目标顶级节点ID，如果是Server则保存业务系统ID，browser则保存应用ID，Browser的模块则保存模块ID，业务则保存业务的ID',
# parent_id=['0','0','0','0']
# target_id=['7839','7804','0','0']      #主机
# target_name=['test-alarm0816','test-alarm-dc0731','192.168.5.71:8080','alarmx']
# target_name1=['pages/index/index']
# target_name2=['demo.tingyun.com/mp-mock/test/custom-code']
# target_name3=['requestPayment']
# target_name4=['pages/index/index/send/alias']
# # agreement_id='2018'
# agreement_id='19'
# alarm_type=['2','1','1'] #1策略告警    2只能告警
# alarm_settings_id=['171','152','172','1100','1144','1147','1148','1149']
# policy_id=['285','258','262','3591','3608','3612','3613','3614']
#
# ts=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# target_type=['1','2','3','4']    #用户体验   #业务分析   #apm
# target_children_type1 = ["BAPP","BM","BHOST","BPG","BAJ","BOP"]  #应用，模块，主机，关键页面，Ajax，关键操作
# target_children_type2=["BZ","BZOP"]   #业务，业务操作
# target_children_type3=['SBZ','SAPP','TX','EXT','IF']   #业务系统，应用，事务，外部服务，服务接口
# target_children_type4=["MAPP","MPG","MAJ","MAPI","MOP"]
# # print target_type[a],target_children_type[a][i],top_level_parent_id[n],parent_id[n],
# target_children_type=[target_children_type1,target_children_type2,target_children_type3,target_children_type4]
# print "target_type,target_children_type,top_level_parent_id,parent_id,target_id,target_name,alarm_type,alarm_settings_id,policy_id",target_type[a],target_children_type[a][i],top_level_parent_id[n],parent_id[n],target_id[n],target_name[n],alarm_type[1],alarm_settings_id[n],policy_id[n]
# #应用
# # sqls="INSERT INTO NL_U_ALARM_EVENTS_TRACE (target_type, target_children_type, top_level_parent_id, parent_id, target_id, target_name, agreement_id, status, read_status, alarm_type, alarm_settings_id, policy_id, begin_time,is_useful, message, ignore_status, sample_group, sample_group_values, ctime, mtime) " \
# #                                         "VALUES ("+target_type[a]+",'"+target_children_type[a][i]+"', '"+top_level_parent_id[n]+"', '"+parent_id[n]+"', '"+target_id[n]+"', '"+target_name[n]+"', '"+agreement_id+"', '1', '0', '"+alarm_type[1]+"', '"+alarm_settings_id[n]+"', '"+policy_id[n]+"', '"+ts+"', '0', '', '0', '1', '', '"+ts+"', '"+ts+"')"
#
# # #关键页面
# # sqls="INSERT INTO NL_U_ALARM_EVENTS_TRACE (target_type, target_children_type, top_level_parent_id, parent_id, target_id, target_name, agreement_id, status, read_status, alarm_type, alarm_settings_id, policy_id, begin_time,is_useful, message, ignore_status, sample_group, sample_group_values, ctime, mtime) " \
# #                                         "VALUES ("+target_type[a]+",'"+target_children_type[a][1]+"', '"+top_level_parent_id[n]+"', '"+parent_id[n]+"', '"+target_id[n]+"', '"+target_name1[0]+"', '"+agreement_id+"', '1', '0', '"+alarm_type[1]+"', '"+alarm_settings_id[4]+"', '"+policy_id[4]+"', '"+ts+"', '0', '', '0', '1', '', '"+ts+"', '"+ts+"')"
#
#
# # #关键请求
# # sqls="INSERT INTO NL_U_ALARM_EVENTS_TRACE (target_type, target_children_type, top_level_parent_id, parent_id, target_id, target_name, agreement_id, status, read_status, alarm_type, alarm_settings_id, policy_id, begin_time,is_useful, message, ignore_status, sample_group, sample_group_values, ctime, mtime) " \
# #                                         "VALUES ("+target_type[a]+",'"+target_children_type[a][3]+"', '"+top_level_parent_id[n]+"', '"+parent_id[n]+"', '"+target_id[n]+"', '"+target_name3[0]+"', '"+agreement_id+"', '1', '0', '"+alarm_type[1]+"', '"+alarm_settings_id[6]+"', '"+policy_id[6]+"', '"+ts+"', '0', '', '0', '1', '', '"+ts+"', '"+ts+"')"
#
#
# #操作
# # sqls="INSERT INTO NL_U_ALARM_EVENTS_TRACE (target_type, target_children_type, top_level_parent_id, parent_id, target_id, target_name, agreement_id, status, read_status, alarm_type, alarm_settings_id, policy_id, begin_time,is_useful, message, ignore_status, sample_group, sample_group_values, ctime, mtime) " \
# #                                         "VALUES ("+target_type[a]+",'"+target_children_type[a][4]+"', '"+top_level_parent_id[n]+"', '"+parent_id[n]+"', '"+target_id[n]+"', '"+target_name4[0]+"', '"+agreement_id+"', '1', '0', '"+alarm_type[1]+"', '"+alarm_settings_id[7]+"', '"+policy_id[7]+"', '"+ts+"', '0', '', '0', '1', '', '"+ts+"', '"+ts+"')"
#
# # print "sqls",type(target_children_type3[a])
# # print "type",type(target_type[a])
#
#
# # print "sqls",sqls
#
# sqls="select * from 表名 limit 1"
#
#
# sqls="INSERT INTO NL_U_ALARM_EVENTS (event_trace_id, related_event_id, event_type, event_level, status, begin_time, ctime) " \
# "VALUES ('"+data1(sqls)+"', '0', '1', '1', '1','"+ts+"','"+ts+"')"
#
# print data1(sqls)
# metric_bapplication=['fst','fpt','drt','pd','rast','rrt','rht','oa','ort','dns','jer','spvr','qps']   #应用指标/模块/主机
# metric_bvapplication=['spv','oec','soc']#应用vip
# metric_bgjoprt=['oa','ort','oc','oec','soc']   #关键操作
# metric_bgjpage=['fst','fpt','drt','pd','rast','rrt','rht','oa','ort','dns','jer','tcp','fp','spvr','qps','spv']#关键页面
#
# metric_miniapp=["oa","ort","rast","jer","net","frt","onrt","rer","rd"]
# MPG=["jer","frt","onrt","cmv"]
# MAJ=["rast","net","rer","rd"]
# MAPI=["msr"]
# MOP=["oa","ort"]
# mini=[metric_miniapp,MPG,MAJ,MAPI,MOP]
# metric3=[]
# warn_rate=[1,2,3]
# Cril_rate=[5,6,7]
# t=data1(sqls)
# # for i in range(len(metric_bapplication)):
# for i in range(len(metric_miniapp)):
#      sqls="INSERT INTO NL_U_ALARM_EVENTS_DETAIL (event_id, metric_id, threshold, value, request_count, compare_type, threshold_type, ctime) " \
#       "VALUES ('"+t+"', '"+mini[0][i]+"', '2', '10', '100', '3', '1', '"+ts+"')"
#
#
#      data1(sqls)
#      print t