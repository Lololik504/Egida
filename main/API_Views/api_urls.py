from django.urls import path, include

from main import FieldsAPI
from main.API_Views.Building import SchoolBuildingsInfo
from main.API_Views.District import *
from main.API_Views.Export import ExportExcel
from main.API_Views.Personal import PersonalOfSchoolInfo, UpdaterPrikazOnly
from main.API_Views.Requisites import RequisitesInfo
from main.API_Views.School import SchoolInfo
from main.API_Views.TEST import TEST
from main.API_Views.Temperature import TemperatureInfo
from main.API_Views.Documents import DocumentsView
from main.API_Views.Orders import RospotrebView, GospozhView, RostechView, SudebView, OtherOrdersView
urlpatterns = [
    path('fields/', include("main.fields_url")),
    path('filters/', FieldsAPI.Filters.as_view()),
    path('school/', SchoolInfo.as_view()),
    path('districts/', DistrictsInfo.as_view()),
    path('districts/query/', DistrictsQuery.as_view()),
    path('district/', OneDistrictInfo.as_view()),
    # path('all_buildings/', SchoolBuildingsInfo.as_view()),
    path('building/', include("main.API_Views.Building.building_urls")),
    path('personal/', PersonalOfSchoolInfo.as_view()),
    path('temperature/', TemperatureInfo.as_view()),
    path('requisites/', RequisitesInfo.as_view()),
    path('export/', ExportExcel.as_view()),
    path('docs/', DocumentsView.as_view()),
    path('TEST/', TEST.as_view(), name="test1"),
    path('orders/rospotreb/', RospotrebView.as_view()),
    path('orders/gospozh/', GospozhView.as_view()),
    path('orders/rostech/', RostechView.as_view()),
    path('orders/sudeb/', SudebView.as_view()),
    path('orders/otherorders/', OtherOrdersView.as_view()),
    path('personal/updater/', UpdaterPrikazOnly.as_view())
]
