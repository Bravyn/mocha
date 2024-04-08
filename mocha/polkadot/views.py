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
        return HttpResponse("Welcome Commander, let's get started, shall we?")
    else:
        return HttpResponse("Your number is not in the system")