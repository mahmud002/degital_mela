from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User,auth
# from sympy import randMatrix
# Create your models here.
class Product(models.Model):
    title=models.TextField(max_length=30, blank=True)
    ram=models.TextField(max_length=30, blank=True)
    rom=models.TextField(max_length=30, blank=True)
    price=models.TextField(max_length=30, blank=True)
    image=models.ImageField(upload_to="dokan/images", default="",null=True, blank=True)
    back_image=models.ImageField(upload_to="dokan/images", default="",null=True, blank=True)
    side_image=models.ImageField(upload_to="dokan/images", default="",null=True, blank=True)