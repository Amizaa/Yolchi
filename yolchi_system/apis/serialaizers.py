from rest_framework import serializers
from yol.models import Driver,Waybill,Car,Report
from yuk.models import Shipper, Advertisement, Route, Cargo
from main.models import CustomUser
from django.contrib.auth.models import User


class DriverSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ("__all__")

class WaybillSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Waybill
        fields = ("__all__")

class CarSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("__all__")

class ReportSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ("__all__")

class ShipperSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = ("__all__")

class AdvertisementSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ("__all__")

class CargoSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ("__all__")

class RouteSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ("__all__")

class UserSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")

class CustomUserSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("__all__")










