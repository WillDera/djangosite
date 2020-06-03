from django.urls import path

from . import views

app_name = 'djangoblog'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/', views.article, name='article'),
    path('article/<slug>/', views.article_detail, name='article_detail'),
]