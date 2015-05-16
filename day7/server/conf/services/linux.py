#!/usr/bin/env python
#linux.py
#def linux os monitor which thing,and Threshold info.
from generic import DefaultService

class DefaultService:
	name = None
	interval = 300
	monitor_dic = {}
	graph_dic = {}
	data_from = 'agent'

class upCheck(DefaultService):
	name = 'upCheck'
	interval = 30
	monitor_dic = {
	'host_status':[None]
	}
#just have data,the host must running.

class memory(DefaultService):
	name = 'memory'
	interval = 60
	monitor_dic = {
		'MemUsage_p':['percentage', 80,90],
		'SwapUsage_p':['percentage', 30,40],
		}

class cpu(DefaultService):
	name = 'cpu'
	interval = 60
	monitor_dic = {
		'iowait':['percentage', 40,60],
		'system':['percentage', 80,90],
		'idle':['percentage', 20,5],
	}
	lt_operator = ['idel']

#lt_operator = [] ,if this sets to empty,all the status will be caculated in > mode,gt = > 






