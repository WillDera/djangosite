from django.urls import path

from . import views

app_name = 'djangoblog'
urlpatterns = [
    path('', views.article, name='index'),
    path('article/', views.article, name='article'),
    path('article/create/', views.article_create, name='create'),
    path('article/<slug>/', views.article_detail, name='article_detail'),
]