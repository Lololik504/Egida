from django.urls import path

from . import API

urlpatterns = [
    path('school/', API.SchoolInfo.as_view()),
    path('districts/', API.DistrictsInfo.as_view()),
    path('district/', API.OneDistrictInfo.as_view()),
    path('building/', API.BuildingInfo.as_view()),
    path('export/', API.ExportExcel.as_view()),
]
