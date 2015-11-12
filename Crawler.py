#!/usr/bin/env  python
# -*- coding : utf-8 -*-

# Script Name:AutoD.py
# Author:Miichy.Liu
# Created:2015.11.11
# Version:0.1

# Description:crawle the nba data from nba.com.cn website

import urllib.request
import urllib.parse
import re

class Crawler:
    url = 'http://china.nba.com/teamindex'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    value = {'gr':'www'}
    data = urllib.parse.urlencode(value).encode('utf-8')

    def __init__(self):
        request = urllib.request.Request(self.url,headers=self.headers)
        response = urllib.request.urlopen(request)
        self.content = response.read()#.decode('utf-8')
        print(self.content)
        print("============")
        #pattern = re.compile(b'<div(.*?)[east|west]-box">(.*?)<h2>(.*?)<ul>(.*?)<li>(.*?)</ul>',re.S)
        #pattern = re.compile(b'<li.*(?=>).*?</li>',re.S)
        pattern = re.compile(b'<a target="_blank" class.*? href.*(?=>).*?</a>',re.S)
        #pattern = re.compile(b'<div(.*?)-box">(.*?)<h2>(.*?)<ul>(.*?)<li>(.*?)<a(.*?)</a>(.*?)</ul>',re.S)
        items = re.findall(pattern,self.content)
        for item in items:
            print(item)

        # url = 'http://www.bing.com/search'
        # values = {'q':'python programming tutorial'}
        # data = urllib.parse.urlencode(values)
        # data = data.encode('utf-8')
        # req = urllib.request.Request(url,data)
        # resp = urllib.request.urlopen(req)
        # respData = resp.read()
        # print(respData)

c = Crawler()