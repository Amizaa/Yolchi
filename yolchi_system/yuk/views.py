from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shipper
from .forms import imageForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import os,re
from django.contrib import messages



@login_required(login_url=reverse_lazy("main:signin"))
def profile(request):
    user = request.user
    shipper = Shipper.objects.get(user=user)
    
    if request.method == "POST":
        if 'info' in request.POST:
            image = request.FILES.get('image')
            phone = request.POST['phone']
            email = request.POST['email']
            
            if image:
                if shipper.profilePicture != 'profile.png':
                    os.remove(shipper.profilePicture.path)
                shipper.profilePicture = image
                shipper.save()
            if phone:
                if re.match(r'09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}', str(phone)):
                    shipper.phone = phone
                    shipper.save()
                else:
                    messages.error(request,'لطفا شماره همراه را صحیح وارد کنید')

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
        'image_url': shipper.profilePicture.url,
        'username': user.username,
        'email': user.email,
        'firstname': user.first_name,
        'lastname': user.last_name,
        'phone': shipper.phone
    }
    return render(request, "yuk/profile.html",context) 

def registerAds(request):
    return render(request, "yuk/register-ad.html")

def route(request):
    return render(request, "yuk/route.html")

def advertisements(request):
    return render(request, "yuk/my-ads.html")

def waybills(request):
    return render(request, "yuk/my-waybills.html")

# Create your views here.
