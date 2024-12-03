from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home (request):
    return render(request, "main/home.html")

# Create your views here.
