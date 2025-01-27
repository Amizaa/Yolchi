from rest_framework import generics,viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated,SAFE_METHODS,BasePermission
from yol.models import Driver,Waybill,Car,Report
from yuk.models import Shipper,Advertisement,Cargo,Route
from main.models import CustomUser
from django.contrib.auth.models import User
from .serialaizers import DriverSerialaizer,CarSerialaizer,WaybillSerialaizer,ReportSerialaizer,ShipperSerialaizer,RouteSerialaizer,AdvertisementSerialaizer,CargoSerialaizer,UserSerialaizer,CustomUserSerialaizer

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class DriverList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Driver.objects.all()
    serializer_class = DriverSerialaizer

class WaybillList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Waybill.objects.all()
    serializer_class = WaybillSerialaizer

class CarList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Car.objects.all()
    serializer_class = CarSerialaizer

class ReportList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Report.objects.all()
    serializer_class = ReportSerialaizer

class ShipperList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerialaizer

class AdvertisementList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerialaizer

class CargoList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Cargo.objects.all()
    serializer_class = CargoSerialaizer

class RouteList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Route.objects.all()
    serializer_class = RouteSerialaizer

class UserList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerialaizer

class CustomUserList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialaizer

class DriverDetail(generics.RetrieveUpdateAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = Driver.objects.all()
    serializer_class = DriverSerialaizer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = Car.objects.all()
    serializer_class = CarSerialaizer

class WaybillDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = Waybill.objects.all()
    serializer_class = WaybillSerialaizer

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = Report.objects.all()
    serializer_class = ReportSerialaizer

class ShipperDetail(generics.RetrieveUpdateAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerialaizer

class AdvertisementDetail(generics.RetrieveUpdateAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerialaizer

class CargoDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = Cargo.objects.all()
    serializer_class = CargoSerialaizer

class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = Route.objects.all()
    serializer_class = RouteSerialaizer

class UserDetail(generics.RetrieveUpdateAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerialaizer

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [IsAuthenticated|ReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialaizer

class DriverViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Driver.objects.all()
    serializer_class = DriverSerialaizer

class ShipperViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerialaizer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerialaizer



# class DetailBook(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerialaizer

