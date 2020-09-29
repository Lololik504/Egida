from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('api/districts', views.HomeView)

urlpatterns = [
    path('', views.index, name='start_page'),
    path('dist', views.district_app, name='start_page'),
    path('district/<str:url>', views.district, name='district'),
    path('district/<str:url>/<int:id>', views.school, name='school')
]

urlpatterns += router.urls