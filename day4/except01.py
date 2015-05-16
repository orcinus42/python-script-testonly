#!/usr/bin/env python
#
class myExcept(Exception):
	pass

while True:
	try:		
		int(raw_input("Please input age:")) 
		#a = ['alex','jack','rain']
		#if "JACK" not in a:
		#	raise myExcept
		break
	except ValueError:
		print "You must input an int."
	except IndexError:
		print "Wrong range..."
	except myExcept:
		print "your age is xxx "
