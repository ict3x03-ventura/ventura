from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, request
from django.template import loader
from django.shortcuts import render
from datetime import date
from base.models import HotelRoom, HotelRoomImages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ventura.settings import RECAPTCHA_PUBLIC_KEY as secret_key
from .decorators import check_recaptcha


# Create your views here.
def index(request):
    today = date.today()
    today = today.strftime("%m/%d/%Y")
    return render(request, 'home.html', {'date_placeholder': today})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@check_recaptcha
def loginPage(request):
    context = {'secret_key': secret_key}
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            print("Username or password does not exist")
        

        user = authenticate(request, username=username, password=password)
        if user is not None and request.recaptcha_is_valid:
            login(request, user)
            return redirect('webindex')
        else:
            messages.error(request, 'Username OR password is incorrect')
            print("Username or password does not exist")
    return render(request, 'login.html', context)

def registerPage(request):
    return render(request, 'register.html')

def account(request):
    return render(request, 'account.html')

def room(request):
    room_list = HotelRoomImages.objects.all().select_related('room')
    context = {'room_list': room_list}
    return render(request, 'room.html', context)

def logoutUser(request):
    logout(request)
    return redirect('webindex')

@login_required(login_url='weblogin')
def booking(request, room_id):
    
    gst_calc = 0.07 
    context = {}
    return render(request, 'payment.html', context)
