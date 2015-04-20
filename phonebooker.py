#!/usr/local/bin/python
import sys
import re
import urllib
import urllib3

full_name = ''
for i in xrange(1,len(sys.argv)):
    full_name += sys.argv[i] + ' '
name = full_name.replace(' ','%20')
url = 'http://phonebook.uconn.edu/results.php?basictext=' + name

http = urllib3.PoolManager()
r = http.request('GET', url)
page_text = r.data

if 'subHead2' in page_text:
    print full_name[:-1] + " is a student."
elif '<div align="left">Status</div>' in page_text:
    print "Too many results."
elif 'records than the maximum allowed' in page_text:
    print "Way too many results."
else:
    print "No results."
