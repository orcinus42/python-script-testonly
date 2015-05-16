#!/usr/bin/env python
#
import SocketServer,time

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print 'Got a connection from:' ,self.client_address[0]
		data_type = self.request.recv(1024)
		print '\033[43;1m Recv client signal: \033[0m',data_type
		if data_type == 'SendMonitorData':
			print '\033[42;1m send back confirmation signal!\033[0m'
			self.request.send('ReadyToRecv')
			status_data = self.request.recv(8192)
			print status_data
		#print self.request.recv(1024)

if __name__ == "__main__":
	host,port = "",7767
	server = SocketServer.ThreadingTCPServer((host,port),MyTCPHandler)
server.serve_forever()

