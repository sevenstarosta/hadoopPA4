#!/usr/bin/env python

from operator import itemgetter
import sys

current_syst = None
current_time= None
current_count = 0
current_temp = 0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if len(line.split('\t')) != 3:
    	continue
    # parse the input we got from mapper.py	
    
    systime, count, temp = line.split('\t')

    syst, time = systime.split(':')
    # convert count (currently a string) to int
    try:
        count = int(count)
	temp = int(temp)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_syst == syst and current_time == time:
        current_count += count
	current_temp += temp
    else:
        if current_syst and current_time:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_syst, current_time, current_temp/float(current_count))
        current_count = count
        current_syst = syst
	current_temp = temp
	current_time = time


# do not forget to output the last word if needed!
if current_syst == syst and current_time == time:
    print '%s\t%s\t%s' % (current_syst, current_time, current_temp/float(current_count))
