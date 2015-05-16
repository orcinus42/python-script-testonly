#!/usr/bin/env python
#data_handle.py
#every 10 sec tell monitor_server_program push data to redis_db.
#coding:utf-8
#and read data to operation from redis_db.

import socket,time,json
import redis_connector as redis
from conf.templates import enabled_templates
from get_monitor_index_dic import monitor_host_dic
host = '172.16.1.105'
port = 7767

print enabled_templates

def send_status_data(action,status_data):
	#send monitor data to server.
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	status_dic = None
	if action == 'pushDataIntoRedis':
		s.send('pushDataIntoRedis')
		server_confirmation = s.recv(1024)
		if server_confirmation == "pushedDataIntoRedis":
			print '\033[33m --------connecting redis to pull out data--------\033[0m'
			status_dic = redis.r.get('STATUS_DATA')
	s.close()
	return status_dic

while True:
	latest_status_dic = send_status_data('pushDataIntoRedis','')
	if latest_status_dic is not None:
		latest_status_dic = json.loads(latest_status_dic)
		for h,t_list in monitor_host_dic.items():
			print h,t_list
			if latest_status_dic.has_key(h):
				print latest_status_dic[h]
			else:
				print "no valid data from %s in DB" % h
	else:
		print '--------err:something is wrong--------'
	time.sleep(10)
