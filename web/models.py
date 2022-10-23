from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
