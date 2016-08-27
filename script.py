# -*- coding: utf_8 -*-

import urllib2
import urllib
import json
import re
import os

DOWNLOAD_URL = 'http://www.packal.org/workflow/wan-qu-ri-bao-fei-guan-fang'
REQUEST_URL = 'http://ns.bigyoo.me/cmd'

def queryData(query):
    # 检测全局变量的版本信息
    clientVersion = os.environ.get('alfred_wanqu_version')

    # 根据用户输入, 构造不同的数据请求
    issue = query
    if issue == 'l':
        params = {"type": "wanqu", "action": "getLatest", "clientVersion": clientVersion}
    elif re.match(r'^r(\d+)?$', issue, re.I):
        matchedData = re.match(r'^r(\d+)?$', issue, re.I)
        if issue == 'r':
            params = {"type": "wanqu", "action": "getRandom", "clientVersion": clientVersion}
        elif matchedData.group(1):
            params = {"type": "wanqu", "action": "getRandom", "count": matchedData.group(1), "clientVersion": clientVersion}
        else:
            print "<items><item><title>输入的什么玩意?..</title><subtitle>正确的输入内容是字母l, 或者字母r, 或者r1类型的字母数字组合, 或者数字</subtitle><icon>icon.png</icon></item></items>"
    elif re.match(r'^\d.*$', issue, re.I):
        params = {"type": "wanqu", "action": "getSpec", "issue": issue, "clientVersion": clientVersion}
    else:
        print "<items><item><title>输入的什么玩意?..</title><subtitle>正确的输入内容是字母l, 或者字母r, 或者r1类型的字母数字组合, 或者数字</subtitle><icon>icon.png</icon></item></items>"

    data = urllib.urlencode(params)
    req = urllib2.Request(REQUEST_URL, data)
    res = urllib2.urlopen(req)
    result = res.read()

    resultDictData = json.loads(result)
    issueTitle = resultDictData['data']['title']

    xmlString = '<items>'
    # 检测是否有新版本, 有新版本更新的情况下, 在数据流中插入升级提醒
    latestVersion = resultDictData.get('version');
    if latestVersion != None and str(latestVersion) != str(clientVersion):
        xmlString += '<item arg="'+ DOWNLOAD_URL +'" valid="YES">'
        xmlString += '<title>New version released!</title>'
        xmlString += '<subtitle>Highly recommend to upgrade your "Wanqu" workflow to the latest version: '+ str(latestVersion) +'!</subtitle>'
        xmlString += '<icon>zangief.png</icon></item>'

    # 构造数据列表
    for item in resultDictData['data']['list']:
        if 'date' in item:
            issueTitle = item['date']

        xmlString += '<item arg="'+ item['link'] +'" valid="YES">'
        xmlString += '<title>'+ item['title'] +'</title>'
        xmlString += '<subtitle>['+ issueTitle +'] ' + item['summary'] +'</subtitle>'
        xmlString += '<icon>icon.png</icon></item>'

    xmlString += '</items>'
    print xmlString
