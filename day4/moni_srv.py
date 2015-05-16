#!/usr/bin/env python
#

from services import *

class defaultModule:
	hostname = None
	ip = None
	monitor_service = [cpu,'memory','load','network']
	graph_list = ['cpu','memory']
	customized_service = None

class host1(defaultModule):
	hostname = 'localhost'
	ip1 = '172.16.1.105'
	customized_service = ['mysql']

class host2(defaultModule):
	hostname = 'jing'
	ip1 = '172.16.1.99'
	customized_service = [cpu,'mongoDB','Nginx']
	customized_service[0].interval = 50


class host3(defaultModule):
	hostname = 'alex'
	ip1 = '172.16.1.100'
#	customized_service = ['mysql']

enable_monitors = (
	host1(),
	host2(),
	host3()
)


for h in enable_monitors:
	print h.hostname,h.ip1,h.customized_service
	c= h.monitor_service[0]
	print "\033[43;1m %s \033[0m" % c
	print c.interval
	print c.index_dic
