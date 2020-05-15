import json
import requests


def generateNews(n):
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=1e2203fa10234d0a999cf82f685ac8d2')
    response = requests.get(url)
    convertdata=response.text
    jsonData = json.loads(convertdata)
    result = ""
    for x in range(n):
        result += '<article><h1>Title:%s</h1><h4>%s</h4></article><br>' % (jsonData["articles"][x]["title"].encode(), jsonData["articles"][x]["description"].encode())
    return result



