from django.contrib import admin
from .models import Driver, Waybill, Report, Car

admin.site.register(Driver)
admin.site.register(Waybill)
admin.site.register(Report)
admin.site.register(Car)
