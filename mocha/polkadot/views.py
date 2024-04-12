from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ImageForm

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

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})

def services(request):
    services_template = loader.get_template("services.html")
    return HttpResponse(services_template.render())
