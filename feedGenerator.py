from feedgen.feed import FeedGenerator
from db import Article, Video, getArticles, getVideos

def generate():
    fg = FeedGenerator()
    fg.id('http://ign.com')
    fg.title('IGN Testfeed')
    fg.author({'name':'Tom Sell', 'email':'tom@example.com'})
    fg.link(href='http://example.com', rel='alternate')
    fg.subtitle('The Code Foo Feed!')
    fg.language('en')

    count = 1
    articles = getArticles()
    for article in articles:
        fe = fg.add_entry()
        fe.id('http://codefoofeed.com/article/' + str(count))
        fe.title(article.headline)
        fe.description(article.subHeadline)
        fe.link(href=article.link, rel='alternate')
        count += 1

    count = 1
    videos = getVideos()
    for video in videos:
        fe = fg.add_entry()
        fe.id('http://codefoofeed.com/video/' + str(count))
        fe.title(video.name)
        fe.description(video.description)
        fe.link(href=video.link, rel='alternate')
        count += 1

    rssfeed = fg.rss_str(pretty=True)
    return rssfeed
