#!/usr/bin/python env
#
import sys
from service import *
base_dir = "/home/jing/jingpy/day7/client"

sys.path.append(base_dir)
enabled_services = {
	'service':(
		('upCheck',upCheckMonitor()),
		('memory',memoryMonitor()),
	)
}
