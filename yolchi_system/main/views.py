from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import CustomUser
from .forms import UserForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def signin(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                if CustomUser.objects.get(user=user).app == 'YOL':
                    return redirect('yol:profile')
                else :
                    return redirect('yuk:profile')

            else:
                messages.error(request, 'نام کاربری یا رمزعبور اشتباه است')
                form = UserForm()
                return render(request, 'main/login.html', {'form': form})   

        else:
            form = UserForm()
            return render(request, 'main/login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user_type = request.POST['userType']
        newuser = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email = email
        )

        try:
            newuser.save()
            if user_type == 'driver':
                CustomUser.objects.create(user=newuser,app='YOL')
                return redirect('yol:profile')
            else :
                CustomUser.objects.create(user=newuser,app='YUK')
                return redirect('yuk:profile')

        except:
            return HttpResponse("خطایی رخ داده است")
    else:
        form = UserRegistrationForm()
        return render(request, 'main/signup.html', {'form': form})



# Create your views here.
