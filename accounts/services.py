import json

from django.urls import resolve
from accounts.models import *
from accounts.serializers import *

from .models import MyUser


def get_user_class(user):
    if user.permission == MyUser.Permissions.SCHOOL.value:
        try:
            return SchoolUser.objects.get(pk=user.pk)
        except:
            return None
    elif user.permission == MyUser.Permissions.DISTRICT.value:
        try:
            return DistrictUser.objects.get(pk=user.pk)
        except:
            return None
    elif user.permission == MyUser.Permissions.DEPARTAMENT.value:
        try:
            return DepartamentUser.objects.get(pk=user.pk)
        except:
            return None
    elif user.permission == MyUser.Permissions.ADMIN.value:
        try:
            return AdminUser.objects.get(pk=user.pk)
        except:
            return None

# def get_user_serialiser(user, many=True):
#     if (type(user) == SchoolUser):
#         return UserSerialiaer(user, many=many)
