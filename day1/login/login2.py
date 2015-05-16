#!/usr/bin/env python
#
import os
account_file = 'account.txt'
lock_file = 'lock.txt'

for i in range(3):
	username = raw_input("username: ").strip()
	password = raw_input("password: ").strip()
	if len(username) != 0 and len(password) != 0:
		f = file(account_file)
		loginSuccess = False
		for line in f.readlines():
			if username == line.split()[0] and password == line.split()[1]:
				print "Welcome %s login my system" % username
				loginSuccess = True
				break
			elif username == line.split()[0]:
				print "Wrong password!"
		if loginSuccess is True:
			break				
	else:
		continue
else:
	l = file(lock_file,'a')
	l.write('%s\n' %username)
	l.close()
