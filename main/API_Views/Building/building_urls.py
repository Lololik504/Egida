from django.urls import path, include

from main.API_Views.Building import *

urlpatterns = [
    path('building_construction/', BuildingConstructionAPI.as_view()),
    path('engineering_communication/', EngineeringCommunicationAPI.as_view()),
    path('indoor_areas/', IndoorAreasAPI.as_view()),
    path('safety_system/', SafetySystemAPI.as_view()),
    path('territory_improvement/', TerritoryImprovementAPI.as_view()),
    path('sport_facilities/', SportsFacilitiesAPI.as_view()),
    path('accessible_environment/', AccessibleEnvironmentAPI.as_view()),
    path('all/', SchoolBuildingsInfo.as_view()),
    path('', BuildingInfo.as_view())
]
