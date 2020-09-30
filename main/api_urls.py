from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('districts/', views.district_app)
]
