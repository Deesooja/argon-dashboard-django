# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class UserImage(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     image=models.FileField(upload_to="user_image")
#     address=models.CharField(max_length=250)
#     city=models.CharField(max_length=250)
#     country=models.CharField(max_length=250)
#     postal_code=models.IntegerField()
#     about_me=models.CharField(max_length=250)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)

class UserRestInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.FileField(upload_to="user_image",null=True)
    background_image=models.FileField(upload_to="user_image",null=True)
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    postal_code=models.IntegerField()
    about_me=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)