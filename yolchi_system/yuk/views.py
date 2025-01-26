from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Shipper,Cargo,Advertisement,Route
from yol.models import Waybill,Report
from .forms import imageForm, AdForm, CargoForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import os,re
from django.contrib import messages
from django.utils import timezone



@login_required(login_url=reverse_lazy("main:signin"))
def profile(request):

    request.session['last_visit'] = timezone.now().isoformat()
    
    last_visit_time = request.session.get('last_visit')
    
    if last_visit_time:
        last_visit_time = timezone.datetime.fromisoformat(last_visit_time)
    else:
        last_visit_time = "---"

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
        'phone': shipper.phone,
        'last_visit': last_visit_time,
    }
    return render(request, "yuk/profile.html",context) 

@login_required(login_url=reverse_lazy("main:signin"))
def registerAds(request,):
    if request.method == "POST":
        user = request.user
        shipper = Shipper.objects.get(user=user)

        title = request.POST['title']
        description = request.POST['description']
        freight = request.POST['freight']

        ad = Advertisement.objects.create(
            title=title,
            shipper=shipper,
            description=description,
            freight=freight)

        weight = request.POST['weight']
        type = request.POST['type']
        value = request.POST['value']
        dimension = request.POST['dimension']
        special_instructions = request.POST['special_instructions']
        
        Cargo.objects.create(
            weight=weight,
            type=type,
            value=value,
            dimension=dimension,
            special_instructions=special_instructions,
            advertisement = ad
        )

        return redirect('yuk:route',ad_id=ad.id)
    else:
        form1 = AdForm()
        form2 = CargoForm()
        return render(request, "yuk/register-ad.html", {'form1': form1,'form2':form2})
        

@login_required(login_url=reverse_lazy("main:signin"))
def route(request,ad_id):
    ad = Advertisement.objects.get(pk=ad_id)

    if request.method == 'POST':
        originCity = request.POST['o-city']
        destCity = request.POST['d-city']
        originAddress = request.POST['o-ad']
        destAddress = request.POST['d-ad']
        duration = request.POST['dur']
        distance = request.POST['dis']

        Route.objects.create(
            origin=originAddress,
            destination=destAddress,
            dest_city=destCity,
            origin_city=originCity,
            distance=distance,
            estimated_time=duration,
            advertisement=ad
        )
        messages.success(request,"آگهی با موفقیت ثبت شد")
        return redirect("yuk:profile")
    else:
        return render(request, "yuk/route.html")

@login_required(login_url=reverse_lazy("main:signin"))
def advertisements(request):
    shipper = Shipper.objects.get(user=request.user)
    advertisements = Advertisement.objects.filter(shipper=shipper)
    ads = []
    for ad in advertisements:
        route = Route.objects.get(advertisement=ad)
        ads.append([ad,route])
        
    return render(request, "yuk/my-ads.html",{'ads':ads})

@login_required(login_url=reverse_lazy("main:signin"))
def waybills(request):
    shipper = Shipper.objects.get(user=request.user)
    ads = Advertisement.objects.filter(shipper=shipper)
    waybills = []

    for ad in ads:
        wb = Waybill.objects.filter(advertisement=ad)
        if wb:
            waybills.append([wb[0],Report.objects.filter(Waybill=wb[0])])

                


    return render(request, "yuk/my-waybills.html",{'waybills':waybills})

