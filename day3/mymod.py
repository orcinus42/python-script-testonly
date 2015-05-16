#!/usr/bin/env python
#

x = 30
def printInfo():
    print x + 30

class MyClass():
	data = 'hello MyClass'
	def __init__(self,who):
		self.name = who
	def printName(self):
		print self.data,self.name

if __name__ == '__main__':
	printInfo()
	ins1 = MyClass('jerry')
	print ins1.data
	print ins1.name
