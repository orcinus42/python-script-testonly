#!/usr/bin/env python
#
contact_dic = {}
with open ('contacts.txt') as f:
	for i in f.readlines():
		line = i.strip().split()
		contact_dic[line[0]] = line[1:]
#print contact_dic.keys()

while True:
	search = raw_input("Search info:").strip()
	if len(search) == 0:continue
	if contact_dic.has_key(search):
		print search, contact_dic[search]
	else:
		info_counter = 0
		if len(search) < 3:
			print "No valid info..."
			continue
		for name,value in contact_dic.items():
			if name.count(search) != 0:
				s_index = name.find(search)
				j = ''
				for i in value:
					i = i.ljust(30)
					j += i
				#print len(name)
				name = name[:s_index] + "\033[32;1m%s\033[0m" % search + name[s_index + len(search):]
				#print len(name)
				print name.ljust(40), j
				info_counter += 1
				continue
			x = ''
			for l in value:
				l = l.ljust(30)
				x += 1
			for y in value:
				if y.count(search) != 0:
					print name.ljust(29), x
					info_counter += 1
					break
		if info_counter == 0:
			print "No valid record..."
		else:
			print "Found %s records..." % info_counter
