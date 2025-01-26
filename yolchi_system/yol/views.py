from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Driver,Car,Waybill,Report
from .forms import imageForm, carForm, reportForm, reportStutusForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import os,re
from django.contrib import messages
from django.db.models import Q
import datetime
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
        'license':driver.licenseCode,
        'last_visit': last_visit_time,
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
        if request.POST['licensePlate']:
            car.licensePlate = request.POST['licensePlate']

        car.save()
        messages.success(request, 'اطلاعات با موفقیت تغییر یافت')


    form = carForm()
    context = {
        'form':form,
        'model': car.model,
        'year': car.year,
        'capacity': car.capacity,
        'type': car.get_type_display(),
        'licensePlate':car.licensePlate
    }
    return render(request, "yol/car.html",context)

@login_required(login_url=reverse_lazy("main:signin"))
def waybills(request):
    driver = Driver.objects.get(user=request.user)
    waybills = Waybill.objects.filter(driver=driver)
    return render(request, "yol/my-waybills.html",{'waybills':waybills})


@login_required(login_url=reverse_lazy("main:signin"))
def cargo(request):
    driver = Driver.objects.get(user=request.user)
    try:
        waybill = Waybill.objects.get(Q(driver=driver) & ~Q(status="A") & ~Q(status="N"))
    except Waybill.DoesNotExist:
        waybill = None
    activeReport = Report.objects.filter(Q(Waybill=waybill) & ~Q(status="S"))
    if request.method == "POST":
        if 'change' in request.POST:
            if waybill.status == 'W':
                waybill.status = 'S'
                waybill.save()
            elif waybill.status == 'S':
                waybill.status = 'T'
                waybill.save()
            elif waybill.status == 'T':
                waybill.status = 'A'
                waybill.delivery_date = datetime.datetime.now()
                waybill.save()
                return redirect('yol:profile')
        if 'report1' in request.POST:
            if activeReport:
                messages.error(request,'شما در حال حاضر گزارش فعال دارید')
            else:
                type = request.POST['type']
                description = request.POST['description']
                Report.objects.create(type=type,description=description,Waybill=waybill)
                waybill.status = 'R'
                messages.success(request,'گزارش ثبت شد')
        if 'report2' in request.POST:
            status = request.POST['status']
            rep = Report.objects.get(Waybill=waybill,status="W")
            rep.status = status
            if status == 'N':
                waybill.status = 'N'
                waybill.save() 
                return redirect("yol:profile")
            else:
                waybill.status = 'T'
                waybill.save()
                rep.save()
                messages.success(request,'وضعیت گزارش تغییر یافت')

            # if status == 'N':


    reports = Report.objects.filter(Waybill=waybill)

    form = reportForm()
    form2 = reportStutusForm()
    if waybill:
        context = {
            "has":True,
            "title":waybill.advertisement.title,
            "status":waybill.get_status_display(),
            "st":waybill.status,
            "w_id":waybill.id,
            "form":form,
            "reports":reports,
            "form2": form2,
        }
    else:
        context = {
            "has":False
        }
    return render(request, "yol/my-cargo.html",context)

def waybillDetail(request,w_id):
    waybill = get_object_or_404(Waybill,pk=w_id)
    return render(request, "yol/way-detail.html",{'wb':waybill})
# Create your views here.
