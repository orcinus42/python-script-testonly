#!/usr/bin/env python
#templates.py 
#def base monitor template,and who use template with which option.

from services import linux

class BaseTemplate:
	name = None
	groups = []
	hosts = []
	service_dic = {}

class LinuxGenericServices(BaseTemplate):
	name = 'LinuxGeneric Services'
	groups = ['BJ','HK']
	hosts = ['localhost']
	servive_dic = {
		'cpu':linux.cpu(),
		'memory':linux.memory(),
		'upCheck':linux.upCheck()
	}


class WindowsGenericServices(BaseTemplate):
	name = 'WindowsGeneric Services'
	groups = ['HK']
	servive_dic = {
		'cpu':linux.cpu(),
		'upCheck':linux.upCheck()
	}

enabled_templates = (
	LinuxGenericServices(),
	WindowsGenericServices(),
	)
