#!/usr/bin/env python
#MonitorServer.py
#monitor system service Program.

import sys,SocketServer,time,json
from conf.hosts import group_dic
import redis_connector as redis

#pull out all the monitored hosts and create a empty dict
host_dic = {}
for group,host_list in group_dic.items():
	for h_name,h_info in host_list.items():
		host_dic[h_name] = {}
#print host_dic
#sys.exit()


class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print 'Got a connection from:' ,self.client_address[0]
		data_type = self.request.recv(1024)
		print '\033[43;1m Recv client signal: \033[0m',data_type
		if data_type == 'SendMonitorData':
			print data_type
			print '\033[42;1m send back confirmation signal!\033[0m'
			self.request.send('ReadyToRecv')
			status_data = json.loads(self.request.recv(8192))
			status_data['last_recv'] = time.time()
			if host_dic.has_key(status_data['hostname']):
				host_dic[status_data['hostname']] = status_data
		elif data_type == 'pushDataIntoRedis':
			print '\033[31m--------going to save data to redis--------done!!!\033[0m'
			redis.r['STATUS_DATA'] = json.dumps(host_dic)

			self.request.send('pushedDataIntoRedis')
			

		for h_name,values in host_dic.items():
			print '\033[44;1m data from---> %s \033[0m' % h_name
			print values





if __name__ == "__main__":
	host,port = "",7767
	server = SocketServer.ThreadingTCPServer((host,port),MyTCPHandler)
server.serve_forever()

