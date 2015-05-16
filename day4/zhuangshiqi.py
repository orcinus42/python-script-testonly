#!/usr/bin/env python
#
import time

def timeit(func):
	def wrapper():
		start = time.clock()
		print start
		func()
		end = time.clock()
		print end
		print "used: ", end - start
	return wrapper

@timeit
def sayhi():
	print "<----Hello ,No one can live for ever!---->"

sayhi()
