#!/usr/bin/env python

import sys, datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split(',')
	try:
		date = words[0].split('/')
		if 8 < int(words[1].split(':')[0]) and int(words[1].split(':')[0]) < 17 and datetime.date(int(date[2]),int(date[0]),int(date[1])).weekday() not in [5,6]:
			print '%s\t%s\t%s' % (words[4].strip(), 1, words[3].strip())
	except:
		continue
