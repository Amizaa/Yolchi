from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Driver,Car
from .forms import imageForm, carForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import os,re
from django.contrib import messages

@login_required(login_url=reverse_lazy("main:signin"))
def profile(request):
    user = request.user
    driver = Driver.objects.get(user=user)
    
    if request.method == "POST":
        if 'info' in request.POST:
            image = request.FILES.get('image')
            phone = request.POST['phone']
            email = request.POST['email']
            license = request.POST['license']
            
            if image:
                if driver.profilePicture != 'yol_pictures/profile.png':
                    os.remove(driver.profilePicture.path)
                driver.profilePicture = image
                driver.save()
            if phone:
                if re.match(r'09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}', str(phone)):
                    driver.phone = phone
                    driver.save()
                else:
                    messages.error(request,'لطفا شماره همراه را صحیح وارد کنید')
                    
            if license:
                driver.licenseCode = license
                driver.save()

            if email:
                user.email = email
                user.save()
            
            messages.success(request, 'اطلاعات با موفقیت تغییر یافت')

        elif 'pass' in request.POST:
            if request.POST['password1'] == request.POST['password2']:
                u = User.objects.get(username__exact=user.username)
                u.set_password(request.POST['password1'])
                u.save()
                messages.success(request, 'رمزعبور با موفقیت  تغییر یافت')
            else:
                messages.error(request,'لطفا رمزعبور را صحیح وارد کنید')
        
    form = imageForm()
    context = {
        'form':form,
        'image_url': driver.profilePicture.url,
        'username': user.username,
        'email': user.email,
        'firstname': user.first_name,
        'lastname': user.last_name,
        'phone': driver.phone,
        'license':driver.licenseCode
    }
    return render(request, "yol/profile.html",context) 

@login_required(login_url=reverse_lazy("main:signin"))
def car(request):
    driver = Driver.objects.get(user=request.user)
    car = Car.objects.get(driver=driver)
    if request.method == "POST":
        if request.POST['model']:
            car.model = request.POST['model']
        if request.POST['year'] and request.POST['year']!= '0':
            car.year = request.POST['year']
        if request.POST['capacity'] and request.POST['capacity']!= '0':
            car.capacity = request.POST['capacity']
        if request.POST['type']:
            car.type = request.POST['type']

        car.save()
        messages.success(request, 'اطلاعات با موفقیت تغییر یافت')


    form = carForm()
    context = {
        'form':form,
        'model': car.model,
        'year': car.year,
        'capacity': car.capacity,
        'type': car.get_type_display(),
    }
    return render(request, "yol/car.html",context)

@login_required(login_url=reverse_lazy("main:signin"))
def waybills(request):
    return render(request, "yol/my-waybills.html")

@login_required(login_url=reverse_lazy("main:signin"))
def cargo(request):
    return render(request, "yol/my-cargo.html")


# Create your views here.
