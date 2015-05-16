#!/usr/bin/env python
#
from SocketServer import TCPServer,StreamRequestHandler,ThreadingMixIn

class Server(ThreadingMixIn,TCPServer):pass

class myhandler(StreamRequestHandler):
	def handle(self):
		addr = self.request.getpeername()
		print "Got connection from :" ,addr
		self.wfile.write("Connected!")
server = Server(('',3389),myhandler)
server.serve_forever()
