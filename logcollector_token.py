import urllib, urllib2
import json
import ssl

BASE_URL = "https://localhost:8088/services/collector"
TOKEN = '382BDCA6-B878-4E95-8D7C-4B6554CE21F0'
headers = {"Authorization" : "Splunk " + TOKEN}
# making Unverified HTTPS request 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
try: 
	splunk_data = {
		'index' : 'main',
		#'host' : ev["from"],
		'host' : 'MAC_WYU', 
		'source' : 'log',
		'sourcetype' : 'collector_stats',
		'event' : {"mmessage": "hello world hello world", "index": "main", "host": "TESING", "sourcetype": "collector_stats", "source": "log"}
		#event = msg
	}
	json_data = json.dumps(splunk_data).encode('utf8')
	request_url= urllib2.Request(BASE_URL, json_data, headers)
	request_open = urllib2.urlopen(request_url, context=ctx, timeout=4)
except Exception:
	pass