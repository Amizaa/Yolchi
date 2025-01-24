from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import CustomUser
from yuk.models import Shipper,Advertisement,Route,Cargo
from yol.models import Driver, Car, Waybill
from .forms import UserForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.db.models import Q

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
            return render(request, 'main/signup.html', {'form': form},)

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
    if request.user.is_authenticated:
        app = CustomUser.objects.get(user=request.user).app
        auth = True
        if Driver.objects.filter(user=request.user):
            isDriver = True
        else:
            isDriver = False
    else:
        auth = False
        isDriver = False
        
    if request.method == "POST":
        search = request.POST['search']
        origin = request.POST['origin']
        destination = request.POST['destination']
        minWeight = request.POST['min-weight'] if request.POST['min-weight'] else 0
        maxWeight = request.POST['max-weight'] if request.POST['max-weight'] else 1000000
        maxFreight = request.POST['max-freight'] if request.POST['max-freight'] else 10000000000
        minFreight = request.POST['min-freight'] if request.POST['min-freight'] else 0

        ads = Advertisement.objects.filter(title__icontains=search,
                                           freight__gte=minFreight,
                                           freight__lte=maxFreight)
        advertisements = []
        for ad in ads:
            route = Route.objects.filter(advertisement=ad,
                                         origin_city__icontains=origin,
                                         dest_city__icontains=destination)
            
            cargo = Cargo.objects.filter(advertisement=ad,
                                         weight__gte=minWeight,
                                         weight__lte=maxWeight,)
            if route and cargo:
                advertisements.append([ad,route[0],cargo[0]])
        
        return render(request, "main/ads.html",{'ads':advertisements,'auth':auth,'isDriver': isDriver,'app':app})


    else:
        ads = Advertisement.objects.filter(status='P')
        advertisements = []

        for ad in ads:
            route = Route.objects.get(advertisement=ad)
            cargo = Cargo.objects.get(advertisement=ad)
            advertisements.append([ad,route,cargo])

        return render(request, "main/ads.html",{'ads':advertisements,'auth':auth,'isDriver': isDriver,'app':app})

def registerWaybill(request,ad_id):
    ad = Advertisement.objects.get(pk=ad_id)
    driver = Driver.objects.get(user=request.user)

    if Waybill.objects.filter(Q(driver=driver,status='W') | Q(driver=driver,status='S') | Q(driver=driver,status='T') | Q(driver=driver,status='R')):
        messages.error(request,'شما در حال حاضر بارنامه فعال دارید')
        return redirect('main:ads')
    else:
        Waybill.objects.create(advertisement=ad,driver=driver)
        ad.status = 'A'
        ad.save()
        messages.success(request,'آگهی با موفقیت پذیرفته شد')
        return redirect('main:home')

# Create your views here.
