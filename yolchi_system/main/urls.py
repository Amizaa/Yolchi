from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('login/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signuot/', views.signout, name='signuot'),
    path('ads/', views.ads, name='ads'),
]
