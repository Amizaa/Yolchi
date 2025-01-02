from django.contrib import admin
from .models import Shipper, Advertisement, Route, Cargo

admin.site.register(Shipper)
admin.site.register(Advertisement)
admin.site.register(Route)
admin.site.register(Cargo)
