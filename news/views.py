from django.shortcuts import render
from django.conf import settings
import json


def index(request):
    return render(request, 'news/index.html')


def article(request, link):
    with open(settings.NEWS_JSON_PATH, "r") as json_file:
        articles = json.loads(json_file.read())
        for list_item in articles:
            if list_item['link'] == link:
                return render(request, 'list_item_page.html', {'news': list_item})