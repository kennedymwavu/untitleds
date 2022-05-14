from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from httplib2 import Http

# Create your views here.
def index(response):
    return HttpResponse("<h1>tech with tim!</h1>")

def v1(response):
    return HttpResponse("<h1>View 1!</h1>")

def v2(response):
    return HttpResponse("<h1>View 2!</h2>")

def v3(response):
    return HttpResponse("<h1>View 3! <br> Final One!</h1>")
