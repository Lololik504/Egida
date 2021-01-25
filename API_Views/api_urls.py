from django.urls import path, include

from API_Views.Building import BuildingInfo, SchoolBuildingsInfo
from API_Views.District import OneDistrictInfo, DistrictsInfo
from API_Views.Export import ExportExcel
from API_Views.Personal import PersonalOfSchoolInfo
from API_Views.School import SchoolInfo
from API_Views.Temperature import TemperatureInfo
from main import API, FieldsAPI

urlpatterns = [
    path('fields/', include("main.fields_url")),
    path('filters/', FieldsAPI.Filters.as_view()),
    path('school/', SchoolInfo.as_view()),
    path('districts/', DistrictsInfo.as_view()),
    path('district/', OneDistrictInfo.as_view()),
    path('all_buildings/', SchoolBuildingsInfo.as_view()),
    path('building/', BuildingInfo.as_view()),
    path('personal/', PersonalOfSchoolInfo.as_view()),
    path('temperature/', TemperatureInfo.as_view()),
    path('export/', ExportExcel.as_view()),
    path('TEST/', API.TEST.as_view(), name="test1"),
]
