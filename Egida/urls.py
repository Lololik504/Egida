from django.contrib import admin
from django.urls import path, include

from main.admin import MyAdmin

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', MyAdmin.urls, name='admin'),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt'))
]
