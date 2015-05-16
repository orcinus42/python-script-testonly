#!/usr/bin/env python
global arg
arg = 1

def func(arg):
	global arg
	arg = 3

func(arg)
print arg
