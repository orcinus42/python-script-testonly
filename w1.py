#coding=utf-8
#!/usr/bin/env python
#
import urllib
from bs4 import BeautifulSoup
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 

def info(x):
	soup = BeautifulSoup(x.decode('gbk'))
	dd = soup.find_all("div",attrs={"class":"list_item clearfix"})
	lst = []
	for i in dd:
		dic = {}
		dic['created_at'] = i.span.get_text()
		dic['title'] = i.h2.a.get_text()
		dic['url'] = i.h2.a.attrs.values()[0]
		lst.append(dic)
	return lst

url = 'http://money.163.com/special/pinglun/'
content = urllib.urlopen(url).read()
print info(content)
