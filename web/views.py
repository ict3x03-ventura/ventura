from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()
mongo_connection_string = os.getenv('MONGO_CONNECTION_STRING')


# Create your views here.
def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render({}, request))

