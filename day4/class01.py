#!/usr/bin/env python
#

class dog:
	def __init__(self,name):
		self.name = name

	def talk(self):
		print "Hello master,my name is %s." % self.name
		self.__auth()
	def eat(self,food_type):
		if food_type == "meat":
			print "Thanks master,i like meat..."
		else:
			print "Your poor stupid guy,we dogg eat only meat..."
	def __auth(self):
		print "Cannot be called outside of the class"
	__mark = 2759

D = dog('sam')
D.talk()
D.eat('apple')
print D._dog__mark
