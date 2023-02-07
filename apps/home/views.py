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

# <----------------------------------------------Start Home Page --------------------------------->

@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    
    def get(self, request, *args, **kwargs):

        context = {}
        try:

            if request.user.is_authenticated :     # <---- Chacking User Logged In Or Not

                context = {'segment': 'index'}

                if UserRestInfo.objects.filter(id=request.user.id).exists():

                    context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                    html_template = loader.get_template('home/index.html')

                    return HttpResponse(html_template.render(context, request))

                html_template = loader.get_template('home/index.html')

                return HttpResponse(html_template.render(context, request))
            else:
                return redirect('/login/')

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/page-404.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))


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

# <----------------------------------------------------------------------End Home Page --------------------------------->


# <---------------------------------------------------------------------Start Icons Page --------------------------------->

class IconsView(View):

    def get(self, request, *args, **kwargs):

        context={}
        try:

            if request.user.is_authenticated:       # <---- Chacking User Logged In Or Not

                context = {'segment': 'icons'}

                if UserRestInfo.objects.filter(id=request.user.id).exists():

                    context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                    html_template = loader.get_template('home/icons.html')

                    return HttpResponse(html_template.render(context, request))

                
                html_template = loader.get_template('home/icons.html')

                return HttpResponse(html_template.render(context, request))
            else:
                return redirect("/login/")

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/page-404.html')
            return HttpResponse(html_template.render(context, request))

        except:
            
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))
   
   
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

class GoogleView(View):
    
    def get(self, request, *args, **kwargs):

        context={}
        try:

            if request.user.is_authenticated:  # <---- Chacking User Logged In Or Not

                context = {'segment': 'map'}

                if UserRestInfo.objects.filter(id=request.user.id).exists():

                    context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                    html_template = loader.get_template('home/map.html')

                    return HttpResponse(html_template.render(context, request))
            
                html_template = loader.get_template('home/map.html')

                return HttpResponse(html_template.render(context, request))
            else:
                return redirect("/login/")
        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/page-404.html')
            return HttpResponse(html_template.render(context, request))

        except:
            
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))


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

# <---------------------------------------------------------------End google Page --------------------------------->


# <------------------------------------------------------------Start Profile Page --------------------------------->

class ProfileView(View):
    
    def get(self, request, *args, **kwargs):

        context={}
        try:

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

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/page-404.html')
            return HttpResponse(html_template.render(context, request))

        except:
            
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))


    def post(self, request, *args, **kwargs):

        context={}
        try:
            if request.user.is_authenticated: # <---- Chacking User Logged In Or Not
            

                if request.META.get("CONTENT_TYPE")=="application/json":    # <---- Chacking Ajax Content Type

                    resive_data=json.loads(request.body.decode('UTF-8'))

                    if User.objects.filter(email=resive_data.get("email",None)).exists(): # <---- Chacking Email Existing or not

                        # <---- Data Updated On User table
                        User.objects.filter(email=resive_data.get("email",None)).update(username=resive_data.get("username"),first_name=resive_data.get("first_name"),last_name=resive_data.get("last_name"))
                        
                        id=User.objects.get(email=resive_data.get("email",None)).id
                
                    if UserRestInfo.objects.filter(id=id).exists(): # <---- Chacking For This User id data alrady Exist or not on "UserRestInfo" Table
                        
                        user_obj=User.objects.filter(email=resive_data.get("email",None))
                        
                        # <---- Data Updated On "UserRestInfo" table
                        user_rest_info_obj=UserRestInfo.objects.filter(id=id).update(address=resive_data.get("address"),city=resive_data.get("city"),country=resive_data.get("country"),postal_code=resive_data.get("postal_code"),about_me=resive_data.get("about_me"))

                        if user_rest_info_obj > 0:

                            # <---- Creating Respose To send Template
                            context["status"]=201
                            context["massage"]="Data inserted"
                            context["massage"]=[]

                        else:

                            # <---- Creating Respose To send Template
                            context["status"]=400
                            context["massage"]="Data not  inserted"
                            context["massage"]=[]
                    else:

                        # <---- data alrady not Exist on "UserRestInfo" Table Then Inserting New data
                        user_obj=User.objects.get(email=resive_data.get("email",None))

                        # <----  Inserting New Data
                        user_rest_info_obj=UserRestInfo.objects.create(user=user_obj,address=resive_data.get("address"),city=resive_data.get("city"),country=resive_data.get("country"),postal_code=resive_data.get("postal_code"),about_me=resive_data.get("about_me"))
                        
                        if user_rest_info_obj.id is not None:

                            context["status"]=201
                            context["massage"]="Data inserted"
                            context["massage"]=[]
                        else:
                            context["status"]=400
                            context["massage"]="Data not  inserted"
                            context["data"]=[]
                else:
                    
                    # <---- Inserting and Updating background image
                    if request.FILES.get("backgroun_image") is not None:

                        print("backgroun_image",request.FILES.get("backgroun_image"))

                        # <---- Checking Image Alrady exist or not 
                        if UserRestInfo.objects.filter(user=request.user.id).exists():

                            user_rest_info=UserRestInfo.objects.get(user=request.user.id)

                            # <---- If Image Alrady exist Update This Image
                            user_rest_info.background_image=request.FILES.get("backgroun_image")

                            user_rest_info.save()

                            url=UserRestInfo.objects.get(user=request.user.id).background_image.url

                            # <---- Creating Respose 
                            context["status"]=201
                            context["massage"]="Data inserted"
                            context["data"]={"url":url}
                        else:

                            # <---- If  Image Not  Alrady exist Then Inserting new row
                            user_rest_info=UserRestInfo.objects.create(user=request.user,background_image=request.FILES.get("backgroun_image"))

                            url=user_rest_info.background_image.url
                            
                            context["status"]=201
                            context["massage"]="Data inserted"
                            context["data"]={"url":url}

                    # <---- Inserting and Updating Profile  image
                    if request.FILES.get("profile_pic") is not None:
                        if UserRestInfo.objects.filter(user=request.user.id).exists():

                            user_rest_info=UserRestInfo.objects.get(user=request.user.id)

                            user_rest_info.profile_pic=request.FILES.get("profile_pic")

                            user_rest_info.save()

                            url=UserRestInfo.objects.get(user=request.user.id).profile_pic.url

                            context["status"]=201
                            context["massage"]="Data inserted"
                            context["data"]={"url":url}
                        else:

                            user_rest_info=UserRestInfo.objects.create(user=request.user,profile_pic=request.FILES.get("profile_pic"))

                            url=user_rest_info.profile_pic.url
                            
                            context["status"]=201
                            context["massage"]="Data inserted"
                            context["data"]={"url":url}
        
                return JsonResponse(context)
            else:
                return redirect("/login/")

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/page-404.html')
            return HttpResponse(html_template.render(context, request))

        except:
            
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))



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

class TableView(View):
    
    def get(self, request, *args, **kwargs):

        try:
            if request.user.is_authenticated:

                context = {'segment': 'tables'}

                if UserRestInfo.objects.filter(id=request.user.id).exists():

                    context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                    html_template = loader.get_template('home/tables.html')

                    return HttpResponse(html_template.render(context, request))
                
                
                html_template = loader.get_template('home/tables.html')

                return HttpResponse(html_template.render(context, request))
            else:
                return redirect("/login/")

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/page-404.html')
            return HttpResponse(html_template.render(context, request))

        except:
            
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))


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

        context={}
        try:
            if request.user.is_authenticated:
                context = {'segment': 'products'}
                if UserRestInfo.objects.filter(id=request.user.id).exists():

                    context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)

                    html_template = loader.get_template('home/product.html')

                    return HttpResponse(html_template.render(context, request))
                
                html_template = loader.get_template('home/product.html')

                return HttpResponse(html_template.render(context, request))
            else:
                return redirect("/login/")

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/page-404.html')
            return HttpResponse(html_template.render(context, request))

        except:
            
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))

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
        logout(request)
        return redirect('/login/')

    
# <----------------------------------------------End LogoutPage --------------------------------->


# <----------------------------------------------Login page  --------------------------------->

# @login_required(login_url="/login/")
# def index(request):
#     context = {'segment': 'index'}

#     if UserRestInfo.objects.filter(id=request.user.id).exists():

#         context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id) 

#         html_template = loader.get_template('home/index.html')

#         return HttpResponse(html_template.render(context, request))

#     html_template = loader.get_template('home/index.html')

#     return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/") 
# def pages(request):
#     context = {}
   
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         if UserRestInfo.objects.filter(id=request.user.id).exists():
#             context['user_rest_info'] = UserRestInfo.objects.get(id=request.user.id)
#         #     print(request.user)
#             print(UserRestInfo.objects.get(id=request.user.id).background_image.url)

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))

