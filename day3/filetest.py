#!/usr/bin/env python
#
nei = '''\
	programming is fun,
	when the work is done,
	if you wanna make your work also fun:
		use python!
'''

f = file('poem.txt','w')
f.write(nei)
f.close()

f = file('poem.txt')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line,
f.close
