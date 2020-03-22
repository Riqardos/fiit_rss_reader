import calendar
from datetime import datetime
from django.shortcuts import render
import feedparser


# Create your views here.

def view_rss(request):
    feed = {}

    if request.POST:
        if request.POST.get("url_name"):
            url = request.POST.get('url_name')
            feed = feedparser.parse(url)
            articles = list(map(lambda x: {
                'title': x['title'],
                'summary': x['summary'],
                'date': datetime.fromtimestamp(calendar.timegm(x['published_parsed'])),
                'seconds': calendar.timegm(x['published_parsed']),
                'img': x['links'][0]['href'],
                'link': x['link']
            }, feed.entries))

            if request.POST.get('sort_name'):
                articles = sorted(articles, key=lambda x: x['seconds'], reverse=True)

            feed = {
                'entries': articles
            }

    return render(request, 'rss_reader/main.html', {'feed': feed})
