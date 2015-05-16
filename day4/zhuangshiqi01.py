#!/usr/bin/env python
#

def deco(f):
	def decc():
		print "haha,haha,haha!"
		f()
		print "Too young too simple,some times naive! If me,must put here a army!"
	return decc

@deco

def sayhi():
	print "Why you smile,my load?"

sayhi()
