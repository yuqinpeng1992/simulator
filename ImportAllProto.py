#!/bin/python
#coding=utf-8
import os
for(dirpath, dirname, filelist) in os.walk("./message"):
	for filename in filelist:
		if filename[-3:] == ".py":
			basename = filename[:-3]
			if basename[-4:] == "_pb2":
				dcename = basename[:-4]
				print "import message." + basename + " as " + dcename
