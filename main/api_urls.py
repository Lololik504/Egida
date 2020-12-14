from django.urls import path, include

from . import API, FieldsAPI

urlpatterns = [
    path('fields/', include("main.fields_url")),
    path('filters/', FieldsAPI.Filters.as_view(), name="test1"),
    path('school/', API.SchoolInfo.as_view()),
    path('districts/', API.DistrictsInfo.as_view()),
    path('district/', API.OneDistrictInfo.as_view()),
    path('all_buildings/', API.SchoolBuildingsInfo.as_view()),
    path('building/', API.BuildingInfo.as_view()),
    path('personal/', API.PersonalOfSchoolInfo.as_view()),
    path('temperature/', API.TemperatureInfo.as_view()),
    path('export/', API.ExportExcel.as_view()),
]
