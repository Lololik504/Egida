from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('districts/', views.districts_api),
    path('districts/<str:district_name>/', views.schools_in_district_api)
]
