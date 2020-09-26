from django.contrib import admin
from django.urls import path, include
import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
