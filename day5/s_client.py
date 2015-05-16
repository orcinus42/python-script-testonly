#!/usr/bin/env python
#
#Echo client program
import socket

HOST = '172.16.1.105'  #The remote host
PORT = 50007  #The sam port as used by the server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

s.sendall('hello,world!')
data = s.recv(1024)
s.close()
print 'Received',repr(data)
