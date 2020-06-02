from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('djangoblog/homepage.html')
    return HttpResponse(template)

def about(request):
    template = loader.get_template('djangoblog/about.html')
    return HttpResponse(template)