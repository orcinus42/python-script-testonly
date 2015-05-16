#!/usr/bin/env python
#
#this is a script for test localhost connect to redis_db.
import redis
r = redis.Redis(host='localhost',port=6379,db=0)
