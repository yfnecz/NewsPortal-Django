from django.shortcuts import render
from django.conf import settings
import json
from itertools import groupby

def index(request):
    return render(request, 'news/index.html')

def news(request):
    date_articles = []
    with open(settings.NEWS_JSON_PATH, "r") as json_file:
        articles = json.loads(json_file.read())
        articles = sorted(articles, key=lambda v: v['created'], reverse=True)
        return render(request, 'news/news.html', {'dates': articles})


def article(request, link):
    with open(settings.NEWS_JSON_PATH, "r") as json_file:
        articles = json.loads(json_file.read())
        for list_item in articles:
            if list_item['link'] == link:
                return render(request, 'list_item_page.html', {'news': list_item})