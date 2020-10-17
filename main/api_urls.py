from django.contrib import admin
from django.urls import path, include, re_path

from . import views, API

urlpatterns = [
    path('school/', API.SchoolInfo.as_view()),
    path('districts/', API.DistrictsInfo.as_view()),
    path('district/', API.OneDistrictInfo.as_view()),
    path('building/', API.BuildingInfo.as_view()),
]
