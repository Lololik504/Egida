from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('school/<int:INN>', views.SchoolInfo.as_view()),
]
