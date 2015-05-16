#!/usr/bin/env python
#
#Echo client program
import socket

HOST = '172.16.1.105'  #The remote host
PORT = 9999  #The sam port as used by the server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
	user_input = raw_input("\033[31mYour message: \033[0m").strip()
	if len(user_input) == 0:continue
	s.sendall(user_input)
	print "\033[32m---send---:\033[0m", user_input
	data = s.recv(1024)
	print data

s.close()
