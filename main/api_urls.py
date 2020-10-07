from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('districts/', views.Districts.as_view()),
    path('school/<int:INN>', views.School.as_view()),
    path('districts/<str:district_name>/', views.Schools.as_view())
]
