from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
]
