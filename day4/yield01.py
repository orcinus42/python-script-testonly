#!/usr/bin/env python
#
import time

def count():
	for i in range(10):
		print "do it!"
		yield i

a = count()
print a.next()
print a.next()
print a.next()
print a.next()
