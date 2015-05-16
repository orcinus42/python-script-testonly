#!/usr/bin/env python
#

l1 = [1,2,3,4,5,6]
f = open('wfile.txt','a')

for i in l1:
	n = str(i**2)
	f.write(n+'\n')
f.close
