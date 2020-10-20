from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('', views.index, name='start_page'),
    path('test/', views.test, name='test'),
    path('api/', include('main.api_urls')),
]
