#!/usr/bin/env pythoni

from script import cpu

class serviceModel:
	interval = 300
	retry = 3
	alert_amount = 5
	graph_list = None

class cpu(serviceModel):
	index_dic = {
		'idle':[20, 10,],
		'system':[80, 90],
		'iowait':[50, 70],
	}
	graph_list = [ 'idle', 'iowait']
	script = cpu.cpuMonitor()

