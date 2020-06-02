from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'djangoblog/homepage.html')

def about(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'djangoblog/about.html')