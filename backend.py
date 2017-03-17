import requests
import peewee
from peewee import *

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

database = os.environ.get("DATABASE")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db = MySQLDatabase(database, user=db_user, passwd=db_password)

class Article(peewee.Model):
    thumbnail = peewee.TextField()
    headline = peewee.TextField()
    url = peewee.TextField()

    class Meta:
        database = db

class Video(peewee.Model):
    thumbnail = peewee.TextField()
    name = peewee.TextField()
    url = peewee.TextField()

    class Meta:
        database = db

db.connect()
# True here means it checks to see if the tables exist before creating them
db.create_tables([Article, Video], True)

def save_article(article):
    try:
        Article.get(Article.headline == article.headline)
        print('article already saved')
    except:
        article.save()
        print('article saved')

def save_video(video):
    try:
        Video.get(Video.name == video.name)
        print('video already saved')
    except:
        video.save()
        print('video saved')


startIndex = 0
count = 20

while (startIndex <= 300):
    r = requests.get('http://ign-apis.herokuapp.com/articles?startIndex='
            + str(startIndex)
            + '0&count='
            + str(count))
    j = r.json()

    for item in j['data']:
        thumbnail = item['thumbnails'][2]['url']
        headline = item['metadata']['headline']
        url = "ign.com/articles/" + item['metadata']['slug']
        a = Article(thumbnail = thumbnail, headline = headline, url = url)
        save_article(a)

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
        thumbnail = item['thumbnails'][2]['url']
        name = item['metadata']['name']
        url = item['metadata']['url']
        v = Video(thumbnail = thumbnail, name = name, url = url)
        save_video(v)

    startIndex += count

db.close()
