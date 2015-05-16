#!/usr/bin/env python
#
import commands

def cpuMonitor():
	cmd = "sar 1 1 | grep : | awk '{print $3,$5,$6,$8}'" 
	status, result = commands.getstatusoutput(cmd)
	return result , status

