#!/usr/bin/env python
#
import time
from multiprocessing import Process,Manager,Lock,Pool


def sayHI(n):
	print "Hello,my name is %s ,how are you?" % n
	time.sleep(2) 

pool = Pool(processes = 10)

print pool.map(sayHI, range(100))
#result = []

#for i in range(1000):
#	result.append(pool.apply_async(sayHI, [i]))

#for k in result:
#	k.get()

