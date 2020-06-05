from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'djangoblog/homepage.html')

def article(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    articles = Article.objects.all().order_by('date')
    return render(request, 'djangoblog/article.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'djangoblog/article_detail.html', {'article': article})

# @login_required decorator prevents non-logged in users from accessing
# the article creation section and redirects them to the
# login page instead.

@login_required(login_url='/accounts/login/')
def article_create(request):
    return render(request, 'djangoblog/article_create.html')