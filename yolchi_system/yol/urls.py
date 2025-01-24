from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('car-info/', views.car, name='car'),
    path('my-waybills/', views.waybills, name='waybills'),
    path('my-cargo/', views.cargo, name='cargo'),
    path('waybill-detail/<int:w_id>/', views.waybillDetail, name='waybillDetail'),
]