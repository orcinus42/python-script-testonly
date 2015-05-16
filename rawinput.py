#!/usr/bin/env python
#
name = raw_input("what's your name?")
age = raw_input("how old are you?")
gender = raw_input("what's your gender?")
job = raw_input("what's your job?")
print "*****************"
print "your name is %s ,it's a good name." % name
print "*****************"
print """Personal info:

	Name  : %s
	Age   : %s
	Gender: %s
	Job   : %s
""" % (name,age,gender,job)
