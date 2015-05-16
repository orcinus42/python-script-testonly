#!/usr/bin/env python
#
import time
from multiprocessing import Process,Manager

name_list = []

def sayHI(m, name,n):
	print "Hello,my name is %s ,how are you?" % name,n
	m.append(n)
	print m

manager = Manager()
l = manager.list()

for i in range(10):
	p = Process(target=sayHI,args=(l, 'alex', i))
	p.start()
	p.join()

print '---->',l
