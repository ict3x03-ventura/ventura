from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse, request, JsonResponse
from django.template import loader
from django.shortcuts import render
from datetime import date
from base.models import HotelRoom, HotelRoomImages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ventura.settings import RECAPTCHA_PUBLIC_KEY as secret_key
from .decorators import check_recaptcha
from .forms import UserForm, UserProfileForm, ContactForm
from django.conf import settings
from dotenv import load_dotenv


load_dotenv()

# Create your views here.
def index(request):
    today = date.today()
    today = today.strftime("%m/%d/%Y")
    return render(request, 'home.html', {'date_placeholder': today})


def about(request):
    return render(request, 'about.html')

@check_recaptcha
def contact(request):
    form = ContactForm()
    alert = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            alert = True

        
    context = {'form': form, 'secret_key': secret_key, 'alert': alert}
    return render(request, 'contact.html', context)

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
    if request.user.is_authenticated:
        return redirect('webindex')
    
    u_form = UserForm()
    p_form = UserProfileForm()
    results = "error"
    message = "Something went wrong. Please check and try again"

    if request.method == 'POST':
        u_form = UserForm(request.POST)
        p_form = UserProfileForm(request.POST)

        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            
            #commit is false is used as userprofile.user can not be null
            up = p_form.save(commit=False)
            up.user = user
            up.save()

            # Mark User profile as inactive until verified
            user.is_active = False
            user.email = user.username
            user.save() 

            # results
            results = "success"
            message = "We sent you an SMS!"
            context = {'results': results, 'message': message}
            return redirect('weblogin')
        else:
            context = {'results': results, 'message': message}
    
    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'register.html', context)

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
