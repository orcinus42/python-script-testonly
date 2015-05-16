#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import urllib,urllib2
import re
#返回网页源代码
def getHtml(url):
	html = urllib2.urlopen(url)
	srcCode = html.read()
	return srcCode

def getImg(srcCode):
	#通过分析网页中的图片地址，对其片建立正则
	pattern = re.compile(r'src="(.*?\.jpg)".*?pic_ext="jpeg"')
	#图片完整路径存储为list
	imgSrc = pattern.findall(srcCode)
	num = 0
	for i in imgSrc:
		urllib.urlretrieve(i,'%s.jpg' % num)
		num += 1
		print "正则下载"
		print i
	print '全部任务完成!'
myUrl = 'http://tieba.baidu.com/p/3698756921?see_lz=1&pn=1'
getImg(getHtml(myUrl))
