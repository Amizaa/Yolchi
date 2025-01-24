from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('login/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('ads/', views.ads, name='ads'),
    path('register-waybill/<int:ad_id>/', views.registerWaybill, name='registerWaybill'),
]
