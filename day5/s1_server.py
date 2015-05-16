#!/usr/bin/env python
#
import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		print "\033[32mgot a connection from:\033[0m", self.client_address[0]
		while True:
			self.data = self.request.recv(1024).strip()
			if not self.data:
				print "\033[31mClient is disconnected..\033[0m",self.client_address[0]
				break
			print self.data
			self.request.sendall(self.data.upper())

if __name__ == "__main__":
	HOST,PORT = "",9999
	server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
server.serve_forever()
