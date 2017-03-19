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
    headline = peewee.TextField()
    subHeadline = peewee.TextField()
    link = peewee.TextField()

    class Meta:
        database = db

class Video(peewee.Model):
    name = peewee.TextField()
    description = peewee.TextField()
    link = peewee.TextField()

    class Meta:
        database = db

# True here means it checks to see if the tables exist before creating them
db.create_tables([Article, Video], True)

def saveArticle(article):
    try:
        Article.get(Article.headline == article.headline)
    except:
        article.save()

def saveVideo(video):
    try:
        Video.get(Video.name == video.name)
    except:
        video.save()

def getArticles():
    return Article.select()

def getVideos():
    return Video.select()
