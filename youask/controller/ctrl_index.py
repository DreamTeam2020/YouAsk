# -*- coding: utf-8 -*-
import json
import requests

def generateNews(num):
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=1e2203fa10234d0a999cf82f685ac8d2')
    response = requests.get(url)
    convertdata=response.text.encode('utf-8')
    jsonData = json.loads(convertdata)
    result = ""
    for x in range(num):
        result += '<article><h1>Title:%s</h1><p>%s</p></article><br>' % (
        jsonData["articles"][x]["title"], jsonData["articles"][x]["description"])
    #result.strip("b'")

    return result


