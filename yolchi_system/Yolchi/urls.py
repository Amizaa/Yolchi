"""
URL configuration for Yolchi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', include(('main.urls','main'), namespace="main")),
    path('yol/', include( ('yol.urls', 'yol'),  namespace="yol") ),
    path('yuk/', include( ('yuk.urls','yuk'),  namespace="yuk")),
    path('api/', include( ('apis.urls','apis'),  namespace="apis")),
    path('api-auth/', include("rest_framework.urls")),
    path('api/v1/dj-rest-auth/', include("dj_rest_auth.urls")),
    path("api/v1/dj-rest-auth/registration", include("dj_rest_auth.registration.urls")),
    path("api/schema/", SpectacularAPIView.as_view(api_version='v1'), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
