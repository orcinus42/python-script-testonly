#!/usr/bin/env python
#
import os
account_file = 'account.txt'
lock_file = 'lock.txt'

#put account in a list
f = file(account_file)
account_list = f.readlines()
f.close()


while True:
	#put locked user into a lock list
	f = file(lock_file)
	lock_list = []
	for i in  f.readlines():
		line = i.strip('\n')
		lock_list.append(line)
	f.close()

	loginSuccess = False
	username = raw_input('user: ').strip()
	if username in lock_list:
		print "Sorry,This username are blockd!"
		break
	for line in account_list:
		line = line.split()
		if line[0] == username:
			for i in range(3):
				password = raw_input('passwd: ').strip()
				if password == line[1]:
					print "Welcome %s login my system!" % username
					loginSuccess = True
					break
			else:
				l = file(lock_file,'a')
				l.write('%s\n' %username)
				l.close()
				print "Entered 3 times Wrong password,going to lock %s !" % username
			if loginSuccess == True:
				break
	if loginSuccess == True:
		break
