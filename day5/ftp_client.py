#!/usr/bin/env python
#
#Echo client program
import socket,time

HOST = '172.16.1.105'  #The remote host
PORT = 9999  #The sam port as used by the server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
	user_input = raw_input("\033[31mYour cmd: \033[0m").strip()
	if len(user_input) == 0:continue
	s.sendall(user_input)
	print "\033[32msending...:\033[0m" , user_input
	data = s.recv(1024)
	if data == 'ReadyToReceviceFile':
		with open(user_input.split()[1]) as f:
			s.sendall(f.read())
			time.sleep(0.5)
			s.send("FileSendDone")
	print data
s.close()
