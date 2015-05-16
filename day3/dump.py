#!/usr/bin/env python
#
import pickle

name_dic = {
	'alex':[29,'IT'],
	'rain':{
			'age':24,
			'job':'slaesmen'
			},
	'jack':999
}

with file('name_dic.pkl','wb') as f:
	pickle.dump(name_dic, f)










