from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def profile(request):
    return render(request, "yol/profile.html")

def car(request):
    return render(request, "yol/car.html")

def waybills(request):
    return render(request, "yol/my-waybills.html")

def cargo(request):
    return render(request, "yol/my-cargo.html")

def ads(request):
    return render(request, "yol/ads.html")

# Create your views here.
