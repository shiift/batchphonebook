#!/usr/local/bin/python
import sys
import re
import csv
import urllib
import urllib3

with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(reader):
        if i != 0:
            full_name = ''
            full_name += row[0] + ' '
            full_name += row[2]

            name = full_name.replace(' ','%20')
            url = 'http://phonebook.uconn.edu/results.php?basictext=' + name

            http = urllib3.PoolManager()
            r = http.request('GET', url)
            page_text = r.data
            sys.stdout.write(row[0] + ',' + row[2] + ',')
            if 'subHead2' in page_text:
                print 'Student,' + re.search('(?<=mailto:).*(?=")',page_text).group(0)
            elif('<div align="left">Status</div>' in page_text or
                'records than the maximum allowed' in page_text):
                print "Multiple,"
            else:
                print "Not Student,"
