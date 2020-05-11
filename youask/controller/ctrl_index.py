import json
import requests

def generateNews(x):
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=1e2203fa10234d0a999cf82f685ac8d2')
    response = requests.get(url)
    jsonData = json.loads(response.text)
    result = ""
    for x in range(x):
        result += '<section><h1>Title:%s</h1><h3>%s</h3></section>' % (
        jsonData["articles"][x]["title"], jsonData["articles"][x]["description"])
    return result



