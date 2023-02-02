# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(UserRestInfo)
class UserRestInfoAdmin(admin.ModelAdmin):
    list_display=["user","profile_pic","background_image","address","city","country","postal_code","about_me"]

