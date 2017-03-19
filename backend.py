import requests
from db import Article, Video, saveArticle, saveVideo

startIndex = 0
count = 20

while (startIndex <= 300):
    r = requests.get('http://ign-apis.herokuapp.com/articles?startIndex='
            + str(startIndex)
            + '0&count='
            + str(count))
    j = r.json()

    for item in j['data']:
        headline = item['metadata']['headline']
        subHeadline = item['metadata']['subHeadline']
        link = "ign.com/articles/" + item['metadata']['slug']
        a = Article(headline = headline, subHeadline = subHeadline, link = link)
        saveArticle(a)

    startIndex += count


startIndex = 0
count = 20

while (startIndex <= 300):
    r = requests.get('http://ign-apis.herokuapp.com/videos?startIndex='
            + str(startIndex)
            + '0&count='
            + str(count))
    j = r.json()

    for item in j['data']:
        name = item['metadata']['name']
        description = item['metadata']['description']
        link = item['metadata']['url']
        v = Video(name = name, description = description, link = link)
        saveVideo(v)

    startIndex += count

