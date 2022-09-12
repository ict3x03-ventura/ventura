from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader

# Create your views here.
def index(request) :
    template = loader.get_template('base.html')
    return HttpResponse("<h1>Indian food is the best</h1>")