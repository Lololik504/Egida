import json

from django.urls import resolve
from accounts.models import *
from accounts.serializers import *

from .models import SchoolUser, District


def get_user_class(user):
    if user.permission == 15:
        try:
            return SchoolUser.objects.get(pk=user.pk)
        except:
            return None
    elif user.permission == 10:
        try:
            return District.objects.get(pk=user.pk)
        except:
            return None

# def get_user_serialiser(user, many=True):
#     if (type(user) == SchoolUser):
#         return UserSerialiaer(user, many=many)
