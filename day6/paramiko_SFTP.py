#!/usr/bin/env python
#use paramiko SFTP send file.

import os,sys,paramiko

host = '172.16.1.61'
port = 22
username = 'jing'
password = '3233'

s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

t = paramiko.Transport((host,port))
t.connect(username=username,password=password)
#pkey_file = '/home/jing/.ssh/id_rsa'
#key = paramiko.RSAKey.from_private_key_file(pkey_file)
#t.connect(username=username,pkey=key)



sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test1.py','test2.pydd')
sftp.put('paramiko_SFTP.py','/tmp/paramiko_SFTP01.txt')
s.close()
