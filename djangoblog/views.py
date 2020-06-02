from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'djangoblog/homepage.html')

def article(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    articles = Article.objects.all().order_by('date')
    return render(request, 'djangoblog/article.html', {'articles': articles})

def article_detail(request, slug):
    return HttpResponse(slug)