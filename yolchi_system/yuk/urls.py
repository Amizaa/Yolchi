from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register-ad/', views.registerAds, name='register ad'),
    path('route/', views.route, name='route'),
    path('my-ads/', views.advertisements, name='advertisements'),
    path('my-waybills/', views.waybills, name='waybills'),
]