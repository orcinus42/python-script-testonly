#!/usr/bin/env python
#
import MySQLdb
try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='3233',db='seminar4')
	cur=conn.cursor()  
	cur.execute('select * from host_list;') 
	
	for line in  cur.fetchall():
		print line
	print '-'*50
	
	cur.execute("insert into host_list values('test22','10.0.0.112','win7')")
	cur.execute('select * from host_list;')
	for line in  cur.fetchall():
	        print line
	print '-'*50

	v_list = [ ]
	for i in range(10):
		v_list.append(("test_host%s" % i, "172.16.1.%s" %i, "centos" ))
	print v_list
	cur.executemany('insert into host_list values(%s,%s,%s)', v_list )
	
	cur.close()
	conn.commit()
	conn.close()
except MySQLdb.Error,e:
	print 'Mysql Error Msg:' ,e
