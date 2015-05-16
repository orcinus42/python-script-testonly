#!/usr/bin/env python
#

def sayHi(name,age,job=None):
	"This program is developed by jinglab!"
	global address
	address = "BeiJing"
	print "Hello,my name is %s ,i am %s years old,my job is %s,what about you?" % (name,age,job)
	return "Function Is Excuted!"

if sayHi("alex",22,'IT') == "Function Is Excuted!":
	print "The program has been excuted successfully."

