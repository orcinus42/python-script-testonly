#!/usr/bin/env python
#use ssh_key_file connect romote host;
import os,sys,paramiko

host = sys.argv[1]
port = 22
username = 'jing'
password = '3233'
cmd = sys.argv[2]

s = paramiko.SSHClient()
s.load_system_host_keys()

pkey_file = '/home/jing/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)
s.connect(host,port,username,pkey=key,timeout=5)
stdin,stdout,stderr = s.exec_command(cmd)
#print Split_line,h.ip,Split_line
cmd_result = stdout.read(),stderr.read()

for line in cmd_result:
    print line,
s.close()
