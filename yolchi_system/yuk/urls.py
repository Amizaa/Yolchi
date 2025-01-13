from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('load-announcement/', views.loadAnnoucement, name='load-announcement'),
    path('route/', views.route, name='route'),
]