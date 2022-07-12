from email.policy import default
from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from accounts.models import *
from virtualSafaris.settings import AUTH_USER_MODEL


# Create your models here.
class Safaris(models.Model):
   
    name = models.CharField(max_length=344)
    description = models.TextField()
    location = models.CharField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('safais-image', null=True)
  
    def __str__(self):
        return self.name


class Payment(models.Model):
    amount = models.PositiveIntegerField(default=100)
    contact = models.PositiveIntegerField(
        null=False, blank=False, unique=True, default=254799735661)

    def __str__(self):
        return f'{self.name} payment'

    def save_payment(self):
        self.save()


class Tourguide(models.Model):

    name = models.CharField(blank=False, default='', max_length=255)
    email = models.CharField(max_length=255, default='')
    location = models.IntegerField(blank=True, default='')
    address = models.CharField(max_length=255, default='')
    safaris = models.ForeignKey(Safaris, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name


# class Profile(models.Model):

#     id = models.IntegerField(User, primary_key=True)
#     full_name = models.CharField(max_length=255, default='')
#     contact = models.PositiveIntegerField(
#         null=False, blank=False, unique=True, default=254799735661)
#     email = models.CharField(max_length=255, default='')
#     bio = models.CharField(max_length=255, default='')
#     profile_image = CloudinaryField(
#         'image', default='https://res.cloudinary.com/albrighthuman/image/upload/v1654536946/hjiaxew1u4pydlw3wljo.jpg')
#     bio = models.TextField(max_length=500, default='', blank=True)
#     address = models.CharField(max_length=100, default='')


class Tourist(models.Model):
    admin = models.ManyToManyField(CustomUser)
    bio = models.TextField(blank=True, default='')
    location = models.CharField(max_length=100,  blank=True, default='')
    phone = models.CharField(max_length=11, unique=True, default='')
    name = models.CharField(blank=False, default='', max_length=255)
    email = models.EmailField(max_length=50, blank=True, default='')
    password = models.CharField(max_length=50, blank=False, default='')
    verified = models.BooleanField(default=False)
    image = CloudinaryField('image',blank=True)

    def __str__(self):
        return self.name


