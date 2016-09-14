
import urllib, urllib2
import ssl
from xml.dom import minidom
import requests

base_url = 'https://localhost:8089/'
username = 'admin'
password = 'admin'
splunk_values = {
	'index' : 'main',
	#'host' : ev["from"],
	'host' : 'TESING', 
	'source' : 'log',
	'sourcetype' : 'collector_stats'
}
#event = msg
event = '''
hello world
'''
# making Unverified HTTPS request 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Login and get the session key
request = urllib2.Request(base_url + '/servicesNS/admin/search/auth/login', 
    data = urllib.urlencode({'username': username, 'password': password}))
server_content = urllib2.urlopen(request,context=ctx, timeout=4)
session_key = minidom.parseString(server_content.read()).\
        getElementsByTagName('sessionKey')[0].childNodes[0].nodeValue
#print "Session Key: %s" % session_key 
# insert data 
url = base_url + 'services/receivers/simple?'+ urllib.urlencode(splunk_values)
r= requests.post(url, data=event, headers = { 'Authorization': ('Splunk %s' %session_key)}, verify = False)
print r.text
