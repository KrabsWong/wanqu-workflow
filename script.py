import re
import urllib2
import urllib
import json

issue = "{query}"
if issue == 'l':
	params = {"type": "wanqu", "action": "getLatest"}
else:
	params = {"type": "wanqu", "action": "getSpec", "issue": issue}

data = urllib.urlencode(params)
req = urllib2.Request('http://bigyoo.me/ns/cmd', data)
res = urllib2.urlopen(req)
result = res.read()

resultDictData = json.loads(result)
issueTitle = resultDictData['data']['title']

alfredData = {"items": []}
for item in resultDictData['data']['list']:
    data = {
        "title": item['title'],
        "subtitle": '['+ issueTitle +'] ' + item['summary'],
        "arg": urllib.unquote(item['link'].decode('utf-8').encode('gb18030')),
        "icon": {
            "path": "icon.png"
        }
    }

    alfredData['items'].append(data.copy())

jsonData = json.dumps(alfredData)
print jsonData
