from django.urls import path

from . import FieldsAPI

urlpatterns = [
    path('school/', FieldsAPI.SchoolFields.as_view()),
    path('district/', FieldsAPI.DistrictFields.as_view()),
    path('building/', FieldsAPI.BuildingFields.as_view()),
    path('personal/', FieldsAPI.BuildingFields.as_view()),
    path('all_models/', FieldsAPI.AllModels.as_view()),
]
