#!/usr/bin/env python
#
#for i in range(3):
n = 0
while n < 10:
	n = n + 1
	print n
	name = raw_input('What is your name? ').strip()
	if len(name) == 0:
		continue
	break
else:
	print "Loop is done!"

age = raw_input('What is your age? ')
gender = raw_input('What is your gender? ').strip()
job = raw_input('What is your job? ')


print """Personal info:

	Name:	%s
	Age :	%d
	Sex :	%s
	Job :	%s
""" % (name,int(age),gender,job)

if age <= 28:
	print "You can have hald day's public holiday!"
elif gender == 'F':
	print "Let me think about it ...."
else:
	print "You are too old to take this holiday!"


