# -*- coding:utf-8 -*-
#!/usr/bin/env python
#
import re,random,urllib,urllib2

url1 = "http://tieba.baidu.com/p/1396098654"

my_headers = [
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
	"Opera/9.27 (Windows NT 5.2; U; zh-cn)",
	"Opera/8.0 (Macintosh; PPC Mac OS X; U; en)",
	"Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0",
	"Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1 16 "
]

def get_content(url,headers):
	r_header = random.choice(headers)
	req = urllib2.Request(url)
	req.add_header("User-Agent",r_header)
	req.add_header("Host","tieba.baidu.com")
	req.add_header("Referer","http://tieba.baidu.com/")
	req.add_header("GET",url)

	content = urllib2.urlopen(req).read()
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



info1 = get_content(url1,my_headers)
#info = get_content('http://tieba.baidu.com/p/2336765453')
print get_images(info1)


#<img pic_type="0" class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=e9e669d9d833c895a67e9873e1127397/71cec9f2b211931356bce1fe64380cd790238d0a.jpg" height="521" width="560">

#http://tieba.baidu.com/p/1396098654
#http://tieba.baidu.com/p/2336765453

