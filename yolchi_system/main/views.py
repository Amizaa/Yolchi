from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

# Create your views here.
