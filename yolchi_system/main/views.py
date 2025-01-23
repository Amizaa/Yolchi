from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import CustomUser
from yuk.models import Shipper
from yol.models import Driver, Car
from .forms import UserForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

def user_information(user):
        if CustomUser.objects.get(user=user).app == 'YUK':
            image = Shipper.objects.get(user=user).profilePicture
        else:
            image = Driver.objects.get(user=user).profilePicture

        context = {
            'auth': True,
            'image_url': image.url,
            'app': CustomUser.objects.get(user=user).app
        }
        return context

def home(request):
    if request.user.is_authenticated:
        return render(request, 'main/home.html', user_information(request.user))
    else:
        return render(request, "main/home.html",{'auth':False})

def about(request):
    if request.user.is_authenticated:
        return render(request, 'main/about.html', user_information(request.user))
    else:
        return render(request, "main/about.html",{'auth':False})

def contact(request):
    if request.user.is_authenticated:
        return render(request, 'main/contact.html', user_information(request.user))
    else:
        return render(request, "main/contact.html",{'auth':False})

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

        if User.objects.filter(username=username).exists() :
            messages.error(request, 'نام کاربری قبلا انتخاب شده است')
            form = UserRegistrationForm()
            return render(request, 'main/signup.html', {'form': form})

        else:
        
            newuser = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = password,
                email = email
            )

            try:
                newuser.save()
                
                user = authenticate(
                    request,
                    username=username,
                    password=password
                )
                login(request, user)

                if user_type == 'driver':
                    CustomUser.objects.create(user=newuser,app='YOL')
                    driver = Driver.objects.create(user=newuser)
                    Car.objects.create(driver=driver)
                    return redirect('yol:profile')
                else:
                    CustomUser.objects.create(user=newuser,app='YUK')
                    Shipper.objects.create(user=newuser)
                    return redirect('yuk:profile')
            except:
                return HttpResponse("خطایی رخ داده است")
    else:
        form = UserRegistrationForm()
        return render(request, 'main/signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('main:home')

def ads(request):
    return render(request, "main/ads.html")
# Create your views here.
