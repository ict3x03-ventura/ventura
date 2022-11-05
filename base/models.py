from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    two_step_active = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.user}'


class HotelRoom(models.Model):
    room_type = models.CharField(max_length=50)
    room_price = models.FloatField()
    room_status = models.BooleanField(default=False)
    room_quantity = models.IntegerField(default=7)
    room_description = models.TextField(default="No description")
    stripe_link = models.TextField()


class Reservations(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    booking_id=models.CharField(max_length=50, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.room}'


class Payments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservations, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user} - {self.reservation} - {self.payment_amount}'


class HotelRoomImages(models.Model):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=250, default=None, blank=True, null=True)

class Feedback(models.Model):
    email = models.CharField(max_length=150, default=None, blank=True, null=True)
    subject = models.TextField(default=None, blank=True, null=True)
    message = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.email} - {self.subject}'

class UserToken(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=250, default=None, blank=True, null=True)
    two_step_code = models.CharField(max_length=6, default=None, blank=True, null=True)

    is_email= models.BooleanField(default=False)
    is_password = models.BooleanField(default=False)
    is_sms = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}'
