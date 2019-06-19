import os
import urllib2
import json

while True:
    ip = input('What is your target IP : ')
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print('')