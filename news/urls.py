from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('news/<int:link>/', views.article, name='list_item'),
]
