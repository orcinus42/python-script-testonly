#!/usr/bin/env python
#
import time
from multiprocessing import Process

def sayHI(name,n):
	time.sleep(2)
	print "Hello,my name is %s ,how are you?" % name,n
for i in range(30):
	p = Process(target=sayHI,args=('alex',i))
	p.start()
