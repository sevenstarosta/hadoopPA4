#!/usr/bin/env python

import sys, datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split(',')
	try:
		print '%s\t%s\t%s' % (words[4].strip(), 1, (float(words[3].strip()) - float(words[2].strip()))**2)
	except:
		continue
