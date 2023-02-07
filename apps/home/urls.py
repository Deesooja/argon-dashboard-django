# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home.views import *

urlpatterns = [

    path('', IndexView.as_view(), name='home'),
    path('icons/', IconsView.as_view(), name='icons'),
    path('google/', GoogleView.as_view(), name='google'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('tables/', TableView.as_view(), name='tables'),
    path('product-page/', ProductView.as_view(), name='product_page'),
    path('user-logout/', LogoutView.as_view(), name='logout'),

]