#!/usr/bin/env python
#
import time
chklist = [ ]
idlist = {0001:'alex' }

class school:
	sname = "jinglabs"
	address = "jinhui,shanghai,china"
	tel = '021-3358588'
	teachers = ['jing','feng']
	def regID(self,s_name):
		latest_id = max(idlist.keys())
		s_id = latest_id + 1
		idlist[s_id] = [s_name]

class student(school):
	def __init__(self,name):
		self.name = name

	def checkin(self,c): # c = current time
		if c <= 930:
			print "\033[42;1m%s\033[0m checked in..." % self.name
			time.sleep(1)
			return self.name
		else:
			print "\033[41;1m%s\033[0m is late..." % self.name
	def pay(sefl):
		print "%s paied tution, the student ID will be created soon!" % self.name

s1 = student('alex')
s2 = student('bob')
s3 = student('cendy')

print "start to check in :::"

c_time = 929
for s in s1,s2,s3:
	chk = s.checkin(c_time)
	if chk is not None:
		chklist.append(chk)
		c_time += 1
#	print s.sname
#	print s.tel
	s.regID(s.name)

print "Now it's ", time.ctime()
print chklist
print idlist
