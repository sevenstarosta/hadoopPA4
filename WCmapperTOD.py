#!/usr/bin/env python

import sys, datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split(',')
	try:
		time = int(words[1].split(':')[0])*100 + int(words[1].split(':')[1])
		print '%s\t%s\t%s' % (words[4].strip() + ':' + str(time), 1, words[3].strip())
	except:
		continue
