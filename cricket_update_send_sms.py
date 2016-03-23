#!/usr/bin/python
import urllib2
import cookielib
from getpass import getpass
import os
import sys
import urllib2
import json
import time

# Goto http://cricscore-api.appspot.com/csa to get the match id
url = 'http://cricscore-api.appspot.com/csa?id=<MATCH_ID>'

while True:
	response = urllib2.urlopen(url)
  	data = json.loads(response.read())
  	username = "<username>"
  	passwd = "<password>"
  	message = data[0]['si']+'\n'+data[0]['de']
  	print message
  	number = "<number>"
  	message = "+".join(message.split(' '))
  	url = 'http://site24.way2sms.com/Login1.action?'
  	data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
  	cj = cookielib.CookieJar()
  	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  	opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
  	try:
		usock = opener.open(url, data)
  	except IOError:
    	print "\nCan not connect to Server."
    	raw_input("\nPress Enter to Exit")
    	sys.exit(1)
  	jession_id = str(cj).split('~')[1].split(' ')[0]
  	send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
  	send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
  	opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
  	try:
    	sms_sent_page = opener.open(send_sms_url,send_sms_data)
  	except IOError:
    	print "\nError While Sending the SMS"
    	sys.exit(1)
  	print "\nSMS SENT"
  	time.sleep(5*60) #sleep for 5 minutes
