from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class HotelRoom(models.Model):
    room_type = models.CharField(max_length=50)
    room_price = models.FloatField()
    room_status = models.BooleanField(default=False)
    room_quantity = models.IntegerField(default=7)
    room_description = models.TextField(default="No description")


class Reservations(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    booking_id=models.CharField(max_length=50, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Payments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class HotelRoomImages(models.Model):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=250, default=None, blank=True, null=True)

