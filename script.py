# -*- coding: utf_8 -*-

import urllib2
import urllib
import json

def queryData(query):
    issue = query
    if issue == 'l':
        params = {"type": "wanqu", "action": "getLatest"}
    elif issue == 'r':
        params = {"type": "wanqu", "action": "getRandom"}
    else:
        params = {"type": "wanqu", "action": "getSpec", "issue": issue}

    data = urllib.urlencode(params)
    req = urllib2.Request('http://bigyoo.me/ns/cmd', data)
    res = urllib2.urlopen(req)
    result = res.read()

    resultDictData = json.loads(result)
    issueTitle = resultDictData['data']['title']

    xmlString = '<items>'
    for item in resultDictData['data']['list']:
        xmlString += '<item arg="'+ item['link'] +'" valid="YES">'
        xmlString += '<title>'+ item['title'] +'</title>'
        xmlString += '<subtitle>['+ issueTitle +'] ' + item['summary'] +'</subtitle>'
        xmlString += '<icon>icon.png</icon></item>'

    xmlString += '</items>'
    print xmlString
