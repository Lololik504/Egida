from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('', views.index, name='start_page'),
    path('test/', views.TEST.as_view(), name='test'),
    path('api/', include('main.API_Views.api_urls')),
    path('fields/', include('main.fields_url')),
]
