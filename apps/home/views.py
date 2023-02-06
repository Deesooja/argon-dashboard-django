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
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth import logout
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import csrf_exempt
# <----------------------------------------------Start Home Page --------------------------------->
# @login_required(login_url="/login/")
# @csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            context = {'segment': 'index'}
            if UserRestInfo.objects.filter(id=request.user.id).exists():

                context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                html_template = loader.get_template('home/index.html')

                return HttpResponse(html_template.render(context, request))

            html_template = loader.get_template('home/index.html')
            return HttpResponse(html_template.render(context, request))
        else:
            return redirect('/login/')
    def post(self, request, *args, **kwargs):
        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        # handle PUT requests
        data = {
            'message': 'This is a PUT request'
        }
        return JsonResponse(data)

    def patch(self, request, *args, **kwargs):
        # handle PATCH requests
        data = {
            'message': 'This is a PATCH request'
        }
        return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        # handle DELETE requests
        data = {
            'message': 'This is a DELETE request'
        }
        return JsonResponse(data)

# <----------------------------------------------End Home Page --------------------------------->

# <----------------------------------------------Start Icons Page --------------------------------->
# @login_required(login_url="/login/")
class IconsView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {'segment': 'icons'}
            if UserRestInfo.objects.filter(id=request.user.id).exists():

                context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                html_template = loader.get_template('home/icons.html')

                return HttpResponse(html_template.render(context, request))

            
            html_template = loader.get_template('home/icons.html')
            return HttpResponse(html_template.render(context, request))
        else:
            return redirect("/login/")
    def post(self, request, *args, **kwargs):
        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        # handle PUT requests
        data = {
            'message': 'This is a PUT request'
        }
        return JsonResponse(data)

    def patch(self, request, *args, **kwargs):
        # handle PATCH requests
        data = {
            'message': 'This is a PATCH request'
        }
        return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        # handle DELETE requests
        data = {
            'message': 'This is a DELETE request'
        }
        return JsonResponse(data)

# <----------------------------------------------End Icons Page --------------------------------->


# <----------------------------------------------Start google Page --------------------------------->
login_required(login_url="/login/")
class GoogleView(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {'segment': 'map'}
            if UserRestInfo.objects.filter(id=request.user.id).exists():

                context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                html_template = loader.get_template('home/map.html')

                return HttpResponse(html_template.render(context, request))
           
            html_template = loader.get_template('home/map.html')
            return HttpResponse(html_template.render(context, request))
        else:
            return redirect("/login/")
    def post(self, request, *args, **kwargs):
        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        # handle PUT requests
        data = {
            'message': 'This is a PUT request'
        }
        return JsonResponse(data)

    def patch(self, request, *args, **kwargs):
        # handle PATCH requests
        data = {
            'message': 'This is a PATCH request'
        }
        return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        # handle DELETE requests
        data = {
            'message': 'This is a DELETE request'
        }
        return JsonResponse(data)
# <----------------------------------------------End google Page --------------------------------->


# <----------------------------------------------Start Profile Page --------------------------------->
# @login_required(login_url="/login/")
# @method_decorator(csrf_exempt, name='dispatch')
class ProfileView(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {'segment': 'profile'}
            if UserRestInfo.objects.filter(id=request.user.id).exists():

                context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                html_template = loader.get_template('home/profile.html')

                return HttpResponse(html_template.render(context, request))
            
            

            html_template = loader.get_template('home/profile.html')

            return HttpResponse(html_template.render(context, request))
        else:
            return redirect("/login/")
    def post(self, request, *args, **kwargs):
        # handle POST requests
        # keys=request.FILES.keys()
        # print(keys)
        # print(request.FILES.keys())
        # for key in keys:
        #     print(key)



        # ----------------------------- start for background image-------------------------------------
        print(request.FILES.get("backgroun_image"))
        print(UserRestInfo.objects.get(user=request.user.id))
        user_rest_info=UserRestInfo.objects.get(user=request.user.id)
        user_rest_info.background_image=request.FILES.get("backgroun_image")
        user_rest_info.save()
        url=UserRestInfo.objects.get(user=request.user.id).background_image.url
        # ----------------------------- end for background image-------------------------------------


        # ----------------------------- start for background image-------------------------------------
        # print(request.FILES.get("profile_pic_input"))
        # print(UserRestInfo.objects.get(user=request.user.id))
        # user_rest_info=UserRestInfo.objects.get(user=request.user.id)
        # user_rest_info.profile_pic=request.FILES.get("profile_pic_input")
        # user_rest_info.save()
        # url=UserRestInfo.objects.get(user=request.user.id).profile_pic.url
        # ----------------------------- end for background image-------------------------------------




        # print(json.loads(request.body.decode('UTF-8')).get("hello"))
        # print(type(request.body))

        # send_data={}
        # resive_data=json.loads(request.body.decode('UTF-8'))
        # print(resive_data)

        # if User.objects.filter(email=resive_data.get("email",None)).exists():
        #     User.objects.filter(email=resive_data.get("email",None)).update(username=resive_data.get("username"),first_name=resive_data.get("first_name"),last_name=resive_data.get("last_name"))
           
        #     id=User.objects.get(email=resive_data.get("email",None)).id
        #     if UserRestInfo.objects.filter(id=id).exists():
        #         user_obj=User.objects.filter(email=resive_data.get("email",None))
        #         user_rest_info_obj=UserRestInfo.objects.filter(id=id).update(address=resive_data.get("address"),city=resive_data.get("city"),country=resive_data.get("country"),postal_code=resive_data.get("postal_code"),about_me=resive_data.get("about_me"))
        #         if user_rest_info_obj > 0:
        #             send_data["user_status"]=True
        #         else:
        #             send_data["user_status"]=False

        #     else:
        #         user_obj=User.objects.filter(email=resive_data.get("email",None))
        #         user_rest_info_obj=UserRestInfo.objects.create(user=user_obj,address=resive_data.get("address"),city=resive_data.get("city"),country=resive_data.get("country"),postal_code=resive_data.get("postal_code"),about_me=resive_data.get("about_me"))
        #         if user_rest_info_obj.id is not None:
        #             send_data["user_rest_info_status"]=True
        #         else:
        #             send_data["user_rest_info_status"]=False


        send_data = {
            'message': 'This is a POST request',
            "url":url
        }
        # print(url)
        return JsonResponse(send_data)

    def put(self, request, *args, **kwargs):
        # handle PUT requests
        data = {
            'message': 'This is a PUT request'
        }
        return JsonResponse(data)

    def patch(self, request, *args, **kwargs):
        # handle PATCH requests
        data = {
            'message': 'This is a PATCH request'
        }
        return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        # handle DELETE requests
        data = {
            'message': 'This is a DELETE request'
        }
        return JsonResponse(data)
# <----------------------------------------------End profile Page --------------------------------->



# <----------------------------------------------Start Table Page --------------------------------->
# login_required(login_url="/login/")
class TableView(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {'segment': 'tables'}
            if UserRestInfo.objects.filter(id=request.user.id).exists():

                context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                html_template = loader.get_template('home/index.html')

                return HttpResponse(html_template.render(context, request))
            
            
            html_template = loader.get_template('home/tables.html')
            return HttpResponse(html_template.render(context, request))
        else:
            return redirect("/login/")
    def post(self, request, *args, **kwargs):
        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        # handle PUT requests
        data = {
            'message': 'This is a PUT request'
        }
        return JsonResponse(data)

    def patch(self, request, *args, **kwargs):
        # handle PATCH requests
        data = {
            'message': 'This is a PATCH request'
        }
        return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        # handle DELETE requests
        data = {
            'message': 'This is a DELETE request'
        }
        return JsonResponse(data)
# <----------------------------------------------End Table Page --------------------------------->




# <----------------------------------------------Start Product Page --------------------------------->
# login_required(login_url="/login/")
class ProductView(View):
    
    def get(self, request, *args, **kwargs):
        # if request.user.authenticated:
        if request.user.is_authenticated:
            context = {'segment': 'products'}
            if UserRestInfo.objects.filter(id=request.user.id).exists():

                context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                html_template = loader.get_template('home/index.html')

                return HttpResponse(html_template.render(context, request))
            
            html_template = loader.get_template('home/product.html')
            return HttpResponse(html_template.render(context, request))
        else:
            return redirect("/login/")
    def post(self, request, *args, **kwargs):
        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)

    def put(self, request, *args, **kwargs):
        # handle PUT requests
        data = {
            'message': 'This is a PUT request'
        }
        return JsonResponse(data)

    def patch(self, request, *args, **kwargs):
        # handle PATCH requests
        data = {
            'message': 'This is a PATCH request'
        }
        return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        # handle DELETE requests
        data = {
            'message': 'This is a DELETE request'
        }
        return JsonResponse(data)
# <----------------------------------------------End Product Page --------------------------------->



# <----------------------------------------------Start Logout Page --------------------------------->
class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        print("logout working")
        logout(request)
        context={}
        # html_template = loader.get_template('accounts/login.html')
        # # html_template = loader.get_template('home/icons.html')
        # return HttpResponse(html_template.render(context, request))
        return redirect('/login/')

    
# <----------------------------------------------End LogoutPage --------------------------------->



# class IconsView(View):
#     def get(self, request, *args, **kwargs):
#         context={}
#         html_template = loader.get_template('home/icons.html')
#         return HttpResponse(html_template.render(context, request))

#         # return render(request, 'home/icons.html')
    
#     def post(self, request, *args, **kwargs):
#         # handle post request
#         # process form data and return response
#         return render(request, 'template_name.html', {'form': form})
    
#     def put(self, request, *args, **kwargs):
#         # handle put request
#         # process form data and return response
#         return render(request, 'template_name.html', {'form': form})
    
#     def delete(self, request, *args, **kwargs):
#         # handle delete request
#         # process form data and return response
#         return render(request, 'template_name.html', {'form': form})




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

