import requests

url = "https://ai-news-global.p.rapidapi.com/get_news/us"

headers = {
    'x-rapidapi-host': "ai-news-global.p.rapidapi.com",
    'x-rapidapi-key': "47e1c2f69fmsh3bf5d0854827f3ep11bd26jsnaa104e8ab8ae"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)