from django.shortcuts import render

def profile(request):
    return render(request, "yuk/profile.html")

def registerAds(request):
    return render(request, "yuk/register-ad.html")

def route(request):
    return render(request, "yuk/route.html")

def advertisements(request):
    return render(request, "yuk/my-ads.html")

def waybills(request):
    return render(request, "yuk/my-waybills.html")

# Create your views here.
