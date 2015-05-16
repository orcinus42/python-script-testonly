#!/usr/bin/env python
#
import sys,socket

#create socket
try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, msg:
#    print "Failed to create socket. Error code:" + str(msg[0]) + "Error message :" + msg[1]
	sys.exit()
print "\033[31msocket is created!\033[0m"

#get host ip and port
host = "www.oschina.net"
port = 80
try:
	r_ip = socket.gethostbyname(host)
except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()
print "\033[32mHost ip of %s is %s. \033[0m " % (host,r_ip)

#connect to host
s.connect((r_ip,port))
print "\033[35mSocket connect to %s on ip %s on %s port. \033[0m " % (host,r_ip,port)

#send data to host
message = "GET / HTTP/1.1\r\n\r\n"
try :
	s.sendall(message)
except socket.error:
	print 'Send failed'
	sys.exit()
print "\033[36mData send is done!\033[0m"

#recv data from host
reply = s.recv(4096)
print reply
















