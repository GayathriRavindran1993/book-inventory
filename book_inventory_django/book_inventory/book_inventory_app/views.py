from django.shortcuts import render

import logging
from django.http import HttpResponse
from django.shortcuts import (render, redirect)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login

from book_inventory_app.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    usersExists = User.objects.filter(name=name).exists()
    print(usersExists ,"users")
    if usersExists:
        logging.info("User Already Existing!!")
        return {
            "status":"Already exists"
        }
    user= User()
    user.user_name = username
    user.password = password
    user.full_name = fullname
    user.role = role
    user.save()
    movies= getMovies()
    logging.info("Registered Successfully!!")
    return {
        "user":user
    }
       


