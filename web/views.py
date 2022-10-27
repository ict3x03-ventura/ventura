from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from django.shortcuts import render
from datetime import date


# Create your views here.
def index(request):
    today = date.today()
    today = today.strftime("%m/%d/%Y")
    return render(request, 'home.html', {'date_placeholder': today})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def payment(request):
    return render(request, 'payment.html')

def account(request):
    return render(request, 'account.html')

def room(request):
    return render(request, 'room.html')

