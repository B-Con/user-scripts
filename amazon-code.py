#!/usr/bin/python

import sys, urllib.parse, urllib.request, datetime

url = 'http://www.amazon.com/gp/feature.html/?ie=UTF8&gcIsProcess=-1&gcpcCode=AAAAA&docId=1000296831#gc'

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:8.0.1) Gecko/20100101 Firefox/8.0.1', \
'Referer' :  'http://www.amazon.com/gp/feature.html/?ie=UTF8&gcIsProcess=-1&docId=1000296831', \
'Cookie' : 'ubid-main=185-9107251-7677747; x-main=zChGDdpZ6NSgCNIQ6nkf6n1nPALMFfGn; apn-user-id=5d0d7e33-0e11-4004-9e42-157e28c56013; session-id-time=2082787201l; session-id=188-4920756-9115709; session-token=mW7gBmjXoUWMVIY7CQxEB5j1jahYUUIgfKlqSl4ArkkQKL4YnDJSpfayWHQNjnMn3lofyL8V4rXSG2D+DaPPTZHTZBmop6V0b8c7fTaO38Kl92y7gvhAgHrDTD1msougpqeIeZaDyE9g8q/wqLpSnOM0TYaYQ7n6B0r9h556fbPwS4kqMa8PGxztJjw9xQ55/f8UC29PpgKxgnj0fjK6tXKW4nTAQJy1mykZ0wOoEP8pRKoQ4a9Fdy0hd50YRO3gkBkKFGD6hF6iBwOuBG/PGQ==; csm-hit=289.57'}

postData = 'CAAAA'
encodedData = urllib.parse.urlencode({'GCPCCodeValue' : postData, 'redirect_path' :'/gp/feature.html/?docId=1000296831'}).encode('ascii')
req = urllib.request.Request(url, encodedData, headers)

outfile = open('/tmp/reply', 'wb')
read = 0

t1 = datetime.datetime.now()
fd = urllib.request.urlopen(req)

while 1:
	responseData = fd.read(1024)
	if read == 0:
		t2 = datetime.datetime.now()
		read = 1
	if not len(responseData):
		break
	outfile.write(responseData)

outfile.close()

c = t2 - t1
sys.stdout.write("Milli = " + str(c.microseconds / 1000) + "\n")
