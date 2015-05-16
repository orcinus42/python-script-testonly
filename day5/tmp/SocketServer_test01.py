#!/usr/bin/env python
#
import SocketServer

#host = ""
#port = 3389

class myhandler(SocketServer.StreamRequestHandler):
	def handle(self):
		addr = self.request.getpeername()
		print "Got connection from :" ,addr
		self.wfile.write("Connected!")
server = SocketServer.TCPServer(('',3389),myhandler)
server.serve_forever()
