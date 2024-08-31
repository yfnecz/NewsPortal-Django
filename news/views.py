from django.shortcuts import render, redirect
from django.conf import settings
import json
from django.views import View
from random import randint
from datetime import datetime


def index(request):
    return redirect('/news/')


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


class NewsCreate(View):

    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'news/news_create.html')

    @staticmethod
    def post(request, *args, **kwargs):
        articles = []
        links_id = 100000
        with open(settings.NEWS_JSON_PATH, "r") as json_file:
            articles = json.loads(json_file.read())
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        articles.append({'created': now, 'text': request.POST['text'],
                         'title': request.POST['title'], 'link': randint(links_id, links_id * 2)})
        with open(settings.NEWS_JSON_PATH, "w") as json_file:
            json_file.write(json.dumps(articles))
        return redirect('/news/')
