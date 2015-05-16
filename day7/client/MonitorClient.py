#!/usr/bin/env python
#
import socket,time,json
from conf.conf import *
host = '172.16.1.105'
port = 7767
hostname = 'localhost'
monitor_dic = {}

def send_status_data(action,status_data):
	#send monitor data to server.
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	if action == 'SendMonitorData':
		s.send('SendMonitorData')
		server_confirmation = s.recv(1024)
		if server_confirmation == "ReadyToRecv":
			s.sendall(status_data)

	print "Sending..."
	data = s.recv(1024)
	print data
	s.close()

for k,v in enabled_services.items():
	if k == 'service':
		for (s_name,s_api) in v:
			monitor_dic[s_name] = {'last_check':0,
									'interval':s_api.interval,
									'plugin':s_api
									}

#			print s_name,s_api,s_api.interval
#			print s_api.plugin.monitor()
#print monitor_dic
#print '*'*50

while True:
	status_dic = {'hostname':hostname}
	for service_name,value_dic in monitor_dic.items():
		print service_name,
		print value_dic['last_check'] + value_dic['interval'] - time.time(),'\033[32m sec to start next round! \033[0m'

		if time.time() - value_dic['last_check'] >= value_dic['interval']:
			#means you need to trigger the next round.
			print "\033[42;1m next round for: \033[0m",service_name
			status_dic[service_name] = value_dic['plugin'].plugin.monitor()
			value_dic['last_check'] = time.time()
			#put the lastest time stamp into monitor.
	if len(status_dic) > 1:
		print '-----------------sending status data to server------------------------'
		send_status_data('SendMonitorData',json.dumps(status_dic))
		"""
		for k,v in  status_dic.items():
			print k
			if k != 'hostname':
				for index,value in v.items():
					print '\t',index,value

		"""
	time.sleep(2)
