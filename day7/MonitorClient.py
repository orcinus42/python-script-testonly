#!/usr/bin/env python
#
import socket

host = '172.16.1.105'
port = 7767
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

user_input = "test data..."
s.sendall(user_input)
print "Sending...",user_input
data = s.recv(1024)
print data

s.close()

