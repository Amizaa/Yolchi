from django.urls import path
from .views import DriverList,WaybillList,CarList,ReportList,ShipperList,AdvertisementList,CargoList,RouteList,UserList,CustomUserList,DriverDetail,CarDetail,WaybillDetail,ReportDetail,ShipperDetail,AdvertisementDetail,CargoDetail,RouteDetail,UserDetail,CustomUserDetail,UserViewSet,ShipperViewSet,DriverViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path("driver-list/", DriverList.as_view(),name="driver_list"),
    path("waybill-list/", WaybillList.as_view(),name="waybill_list"),
    path("car-list/", CarList.as_view(),name="car_list"),
    path("report-list/", ReportList.as_view(),name="report_list"),
    path("shipper-list/", ShipperList.as_view(),name="shipper_list"),
    path("advertisement-list/", AdvertisementList.as_view(),name="advertisement_list"),
    path("cargo-list/", CargoList.as_view(),name="cargo_list"),
    path("route-list/", RouteList.as_view(),name="route_list"),
    path("user-list/", UserList.as_view(),name="user_list"),
    path("custom-user-list/", CustomUserList.as_view(),name="custom_user_list"),

    path("driver-detail/<int:pk>", DriverDetail.as_view(),name="driver_detail"),
    path("waybill-detail/<int:pk>", WaybillDetail.as_view(),name="waybill_detail"),
    path("report-detail/<int:pk>", ReportDetail.as_view(),name="report_detail"),
    path("car-detail/<int:pk>", CarDetail.as_view(),name="car_detail"),
    path("shipper-detail/<int:pk>", ShipperDetail.as_view(),name="shipper_detail"),
    path("advertisement-detail/<int:pk>", AdvertisementDetail.as_view(),name="advertisement_detail"),
    path("cargo-detail/<int:pk>", CargoDetail.as_view(),name="cargo_detail"),
    path("route-detail/<int:pk>", RouteDetail.as_view(),name="route_detail"),
    path("user-detail/<int:pk>", UserDetail.as_view(),name="user_detail"),
    path("custom-user-detail/<int:pk>", CustomUserDetail.as_view(),name="custom_user_detail"),
]

router = SimpleRouter()
router.register("users",UserViewSet,basename="users")
router.register("shippers",ShipperViewSet,basename="shippers")
router.register("drivers",DriverViewSet,basename="drivers")
urlpatterns += router.urls