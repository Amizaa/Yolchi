from django.shortcuts import render

def profile(request):
    return render(request, "yuk/profile.html")

def loadAnnoucement(request):
    return render(request, "yuk/load-announcement.html")

def route(request):
    return render(request, "yuk/route.html")

def advertisements(request):
    return render(request, "yuk/advertisements.html")

def waybills(request):
    return render(request, "yuk/waybill.html")
# Create your views here.
