import os
import sys
import json

#print(sys.version)
#print(sys.executable)

import requests

payload = dict(key1='value1', key2='value2')
#print(payload)
'''
with open('test.json', 'w') as fw:
    json.dump(payload,fw,indent=True)
'''
with open('test.json') as fr:
    conf = json.load(fr)

print(conf['key1'])

p_json = json.dumps(payload, indent=2)
print(p_json)

#r = requests.post('https://httpbin.org/post', data=payload)
#print(r.text)
