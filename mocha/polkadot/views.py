from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def index_page(request):
    home_template = loader.get_template('index.html')
    return HttpResponse(home_template.render())

def number(request, num):
    if num == 12:
        slides = loader.get_template("slides.html")
        return HttpResponse(slides.render())
    else:
        return HttpResponse("Your number is not in the system")
