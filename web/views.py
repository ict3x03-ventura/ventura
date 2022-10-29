from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from django.shortcuts import render
from datetime import date
from base.models import HotelRoom, HotelRoomImages

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
    room_list = HotelRoomImages.objects.all().select_related('room')
    image_list = []
    for roomid in range (room_list.count()):
        image_list.append(room_list[roomid].image_path)
    return render(request, 'room.html', {'room_list': room_list, 'image_list': image_list})

