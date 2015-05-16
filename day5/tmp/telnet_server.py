#!/usr/bin/env python
#
import sys,socket

host = ""
port = 3389

#create socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind socket to host with port
try:
    s.bind((host,port))
except socket.error , msg:
#    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print "\033[31msocket is bind to %s with port %s complete. \033[0m" %(host,port)

#listen in port
s.listen(5)
print "\033[32mNow listening in  port %s . \033[0m" % port

#accept connection
conn,addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

#let lt talk with client
#data = conn.recv(4096)
#reply = 'you said: ' + data
#conn.sendall(reply)

#let server running and donot auto exit
while 1:
	data = conn.recv(4096)
	reply = 'you said: ' + data
	if not data:
		break
	conn.sendall(reply)

conn.close()
s.close()
