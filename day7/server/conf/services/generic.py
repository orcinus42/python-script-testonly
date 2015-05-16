#!/usr/bin/env python
#
class DefaultService:
	name = None
	interval = 300
	monitor_dic = {}
	graph_dic = {}
	data_from = 'agent'

	lt_operator = []
	warning_retry = 3
	critical_retry = 1

#lt_operator = [] ,if this sets to empty,all the status will be caculated in > mode,gt = > 
