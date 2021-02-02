from django.urls import path, include

from main.API_Views.EngineeringCommunication import EngineeringCommunicationAPI
from main.API_Views.IndoorAreas import IndoorAreasAPI
from main.API_Views.SafetySystem import SafetySystemAPI
from main.API_Views.TerritoryImprovement import TerritoryImprovementAPI
from main.API_Views.Requisites import RequisitesInfo
from main.API_Views.TEST import TEST
from main.API_Views.Building import BuildingInfo, SchoolBuildingsInfo
from main.API_Views.District import *
from main.API_Views.Export import ExportExcel
from main.API_Views.Personal import PersonalOfSchoolInfo
from main.API_Views.School import SchoolInfo
from main.API_Views.Temperature import TemperatureInfo
from main.API_Views.BuildongConstruction import BuildingConstructionAPI
from main import FieldsAPI

urlpatterns = [
    path('fields/', include("main.fields_url")),
    path('filters/', FieldsAPI.Filters.as_view()),
    path('school/', SchoolInfo.as_view()),
    path('districts/', DistrictsInfo.as_view()),
    path('districts/query/', DistrictsQuery.as_view()),
    path('district/', OneDistrictInfo.as_view()),
    path('all_buildings/', SchoolBuildingsInfo.as_view()),
    path('building/building_construction/', BuildingConstructionAPI.as_view()),
    path('building/engineering_communication/', EngineeringCommunicationAPI.as_view()),
    path('building/indoor_areas/', IndoorAreasAPI.as_view()),
    path('building/safety_system/', SafetySystemAPI.as_view()),
    path('building/territory_improvement/', TerritoryImprovementAPI.as_view()),
    path('building/', BuildingInfo.as_view()),
    path('personal/', PersonalOfSchoolInfo.as_view()),
    path('temperature/', TemperatureInfo.as_view()),
    path('requisites/', RequisitesInfo.as_view()),
    path('export/', ExportExcel.as_view()),
    path('TEST/', TEST.as_view(), name="test1"),
]
