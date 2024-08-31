from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("news/", views.news, name='news'),
    path('news/<int:link>/', views.article, name='list_item'),
    path('news/create/', views.NewsCreate.as_view(), name='create_news'),
]
