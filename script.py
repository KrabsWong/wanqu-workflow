# -*- coding: utf_8 -*-

import urllib2
import urllib
import json
import re

def queryData(query):
    issue = query
    if issue == 'l':
        params = {"type": "wanqu", "action": "getLatest"}
    elif re.match(r'^r(\d+)?$', issue, re.I):
        matchedData = re.match(r'^r(\d+)?$', issue, re.I)
        if issue == 'r':
            params = {"type": "wanqu", "action": "getRandom"}
        elif matchedData.group(1):
            params = {"type": "wanqu", "action": "getRandom", "count": matchedData.group(1)}
        else:
            print "<items><item><title>输入的什么玩意?..</title><subtitle>正确的输入内容是字母l, 或者字母r, 或者r1类型的字母数字组合, 或者数字</subtitle><icon>icon.png</icon></item></items>"
    elif re.match(r'^\d.*$', issue, re.I):
        params = {"type": "wanqu", "action": "getSpec", "issue": issue}
    else:
        print "<items><item><title>输入的什么玩意?..</title><subtitle>正确的输入内容是字母l, 或者字母r, 或者r1类型的字母数字组合, 或者数字</subtitle><icon>icon.png</icon></item></items>"

    data = urllib.urlencode(params)
    req = urllib2.Request('http://bigyoo.me/ns/cmd', data)
    res = urllib2.urlopen(req)
    result = res.read()

    resultDictData = json.loads(result)
    issueTitle = resultDictData['data']['title']

    xmlString = '<items>'
    for item in resultDictData['data']['list']:
        if 'date' in item:
            issueTitle = item['date']

        xmlString += '<item arg="'+ item['link'] +'" valid="YES">'
        xmlString += '<title>'+ item['title'] +'</title>'
        xmlString += '<subtitle>['+ issueTitle +'] ' + item['summary'] +'</subtitle>'
        xmlString += '<icon>icon.png</icon></item>'

    xmlString += '</items>'
    print xmlString
