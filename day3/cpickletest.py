#!/usr/bin/env python
#
import cPickle as p

shoplist = ['apple','phone','bannana']
shoplistfile = "shoplist.txt"

f = file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()
del shoplist

f = file(shoplistfile)
storefile = p.load(f)
print storefile
f.close()
