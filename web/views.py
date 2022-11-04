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
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .mixins import FormErrors, RedirectParams, TokenGenerator, CreateEmail, ActivateTwoStep
import json


load_dotenv()

'''
Index Views of Ventura
'''
def index(request):
    today = date.today()
    today = today.strftime("%m/%d/%Y")
    return render(request, 'home.html', {'date_placeholder': today})


'''
Login Views of Ventura
'''
def about(request):
    return render(request, 'about.html')



'''
Contact us Views of Ventura
'''
@check_recaptcha
def contact(request):
    form = ContactForm()
    alert = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            messages.success(request, 'Your message has been sent!')
            form.save()
        
    context = {'form': form, 'secret_key': secret_key, 'alert': alert}
    return render(request, 'contact.html', context)



'''
Login Views of Ventura
'''
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


'''
Registration Page of Ventura
'''
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

            # create new token
            token = TokenGenerator()
            make_token = token.make_token(user)
            url_safe = urlsafe_base64_encode(force_bytes(user.pk)) 

            # create and send sms code
            sms_code = ActivateTwoStep(user=user, token=make_token)

            # results
            results = "success"
            message = "We sent you an SMS!"
            context = {'results': results, 'message': message, 'url_safe': url_safe, 'make_token': make_token}
        else:
            message = FormErrors(u_form, p_form)
            context = {'results': results, 'message': message}
        return HttpResponse(
            json.dumps(context),
            content_type="application/json"
        )
    
    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'register.html', context)

def account(request):
    return render(request, 'account.html')

'''
List of rooms views in Ventura
'''
def room(request):
    room_list = HotelRoomImages.objects.all().select_related('room')
    context = {'room_list': room_list}
    return render(request, 'room.html', context)


'''
Logout views of Ventura
'''
def logoutUser(request):
    logout(request)
    return redirect('webindex')


'''
Payment views of Ventura
'''
@login_required(login_url='weblogin')
def booking(request, room_id):
    
    gst_calc = 0.07 
    context = {}
    return render(request, 'payment.html', context)
