from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'djangoblog/homepage.html')

def article(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    articles = Article.objects.all().order_by('date')
    return render(request, 'djangoblog/article.html', {'articles': articles})