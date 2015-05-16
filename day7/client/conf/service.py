#!/usr/bin/python env
#
import conf 
from plugins import cpu,upCheck,memory


class MonitorBase:
	interval = 300
	plugin = None


class upCheckMonitor(MonitorBase):
	interval = 10
	plugin = upCheck

class memoryMonitor(MonitorBase):
	interval = 60
	plugin = memory

class cpuMonitor(MonitorBase):
	interval = 120
	plugin = cpu


