from django.urls import path
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('This is index page')

def index2(request):
    return HttpResponse('This is index2 page')    

def index3(request):
    return HttpResponse('This is index3 page')    