# -*- coding: utf-8 -*-
import json
import requests

def generateNews(num):
    # Generates html code containing various news articles depending on given number
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=1e2203fa10234d0a999cf82f685ac8d2')
    response = requests.get(url)
    convert_data=response.text
    json_data = json.loads(convert_data)
    result = ""
    for field in range(num):
        result += '<article><h1>Title:%s</h1><p>%s</p></article>' % (
            json_data["articles"][field]["title"], json_data["articles"][field]["description"])
    #result.strip("b'")

    return result


