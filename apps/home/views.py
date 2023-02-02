# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    if UserRestInfo.objects.filter(id=request.user.id).exists():
        context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)
        html_template = loader.get_template('home/index.html')
        return HttpResponse(html_template.render(context, request))

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def profile(request):
#     context = {'segment': 'index'}

#     html_template = loader.get_template('home/profile.html')
#     return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # print(request.POST)
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        print(load_template)
        # print(request.POST)
        print(request.method)

        if request.method == "POST":
            # print("indide the if ",request.method)
            # print(request.POST)

            # print(request.POST["email"])
            email=request.POST["email"]
            # print(email)
            user_name=request.POST["user_name"]
            # print(user_name)
            first_name=request.POST["first_name"]
            # print(first_name)
            last_name=request.POST["last_name"]
            # print(last_name)
            address=request.POST["address"]
            # print(address)
            city=request.POST["city"]
            # print(city)
            country=request.POST["country"]
            # print(country)
            postal_code=request.POST["postal_code"]
            # print(postal_code)
            about_me=request.POST["about_me"]
            # print(about_me)

            if User.objects.filter(email=email).exists():
                user_obj=User.objects.get(email=email)
                user_obj.username=user_name
                user_obj.first_name=first_name
                user_obj.last_name=last_name
                user_obj.save()
                if UserRestInfo.objects.filter(id=user_obj.id).exists():
                    user_rest_info=UserRestInfo.objects.get(id=user_obj.id)
                    user_rest_info.address=address
                    user_rest_info.city=city
                    user_rest_info.country=country
                    user_rest_info.postal_code=postal_code
                    user_rest_info.about_me=about_me
                    user_rest_info.save()
                    context['user_rest_info'] = user_rest_info
                else:
                    created=UserRestInfo.objects.create(user_id=user_obj.id,address=address,city=city,country=country,postal_code=postal_code,about_me=about_me)
                    context['user_rest_info'] = created
            html_template = loader.get_template('home/' + load_template)
            return HttpResponse(html_template.render(context, request))

            

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        if UserRestInfo.objects.filter(id=request.user.id).exists():
            context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)
        #     print(request.user)
            print(UserRestInfo.objects.get(id=request.user.id).background_image.url)

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

