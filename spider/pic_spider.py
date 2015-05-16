# -*- coding:utf-8 -*-
#!/usr/bin/env python
#
import re,urllib

def get_content(url):
	"""doc"""
	html = urllib.urlopen(url)
	content = html.read()
	html.close()
	return content

def get_images(info):
	"""doc"""

	regex = r'class="BDE_Image" src="(.+?\.jpg)"'
	pat = re.compile(regex)

	images_code = re.findall(pat,info)
	i = 0
	for image_url in images_code:
		print image_url
		urllib.urlretrieve(image_url,'/tmp/pic/%s.jpg' % i)
		i += 1



info = get_content('http://tieba.baidu.com/p/2772656630')
#info = get_content('http://tieba.baidu.com/p/1396098654')
#info = get_content('http://tieba.baidu.com/p/2336765453')
print get_images(info)


#<img pic_type="0" class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=e9e669d9d833c895a67e9873e1127397/71cec9f2b211931356bce1fe64380cd790238d0a.jpg" height="521" width="560">

#http://tieba.baidu.com/p/1396098654
#http://tieba.baidu.com/p/2336765453

