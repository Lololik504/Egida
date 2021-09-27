from django.urls import path

from . import FieldsAPI

urlpatterns = [
    path('school/', FieldsAPI.SchoolFields.as_view()),
    path('district/', FieldsAPI.DistrictFields.as_view()),
    path('building/', FieldsAPI.BuildingFields.as_view()),
    path('personal/', FieldsAPI.BuildingFields.as_view()),
    path('all_models/', FieldsAPI.AllModels.as_view()),
    path('building_construction/', FieldsAPI.BuildingConstructionFields.as_view()),
    path('engineering_communication/', FieldsAPI.EngineeringCommunicationFields.as_view()),
    path('indoor_areas/', FieldsAPI.IndoorAreasFields.as_view()),
    path('safety_system/', FieldsAPI.SafetySystemFields.as_view()),
    path('territory_improvement/', FieldsAPI.TerritoryImprovementFields.as_view()),
    path('sports_facilities/', FieldsAPI.SportsFacilitiesFields.as_view()),
    path('accessible_environment/', FieldsAPI.AccessibleEnvironmentFields.as_view()),
    path('zppp/', FieldsAPI.ZPPPFields.as_view()),
]
