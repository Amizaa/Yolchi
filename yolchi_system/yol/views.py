from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def profile(request):
    return render(request, "yol/profile.html")


# Create your views here.
