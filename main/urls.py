from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='start_page'),
    path('district/<str:url>', views.district, name='district'),
    path('district/<str:url>/<int:id>', views.school, name='school')
]
