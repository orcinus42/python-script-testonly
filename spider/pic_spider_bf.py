# -*- coding:utf-8 -*-
#!/usr/bin/env python
#
import urllib
from bs4 import BeautifulSoup

def get_content(url):
	"""doc"""
	html = urllib.urlopen(url)
	content = html.read()
	html.close()
	return content

def get_images(info):
	"""doc"""
	soup = BeautifulSoup(info)
	all_img = soup.find_all('img',class_="BDE_Image")
	x = 0
	for im in all_img:
		print im
		image_name = '/tmp/pic/%s.jpg' % x
		urllib.urlretrieve(im['src'],image_name)
		x += 1
		



#info = get_content('http://tieba.baidu.com/p/1396098654')
info = get_content('http://tieba.baidu.com/p/2336765453')
print get_images(info)




#<img pic_type="0" class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=e9e669d9d833c895a67e9873e1127397/71cec9f2b211931356bce1fe64380cd790238d0a.jpg" height="521" width="560">

#http://tieba.baidu.com/p/1396098654
#http://tieba.baidu.com/p/2336765453
