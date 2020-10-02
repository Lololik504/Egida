from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('districts/', views.Districts.as_view()),
    path('districts/<str:district_name>/', views.schools_in_district_api)
]
