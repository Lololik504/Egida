from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='start_page'),
    re_path('district/', views.district, name='district')
]
