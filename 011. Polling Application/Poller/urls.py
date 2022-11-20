from django.contrib import admin
from django.urls import path,include
from auth import urls
from main import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('auth.urls')),
    path('',include('main.urls'))
]
