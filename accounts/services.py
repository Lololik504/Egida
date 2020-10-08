import json

from django.urls import resolve
from accounts.models import *
from accounts.serializers import *

from .models import SchoolUser, District


def get_user_class(username, permission):
    if (permission==15):
        try:
            return SchoolUser.objects.get(username=username)
        except:
            return None
    elif (permission == 10):
        try:
            return District.objects.get(username=username)
        except:
            return None


def get_user_serialiser(user, many=True):
    if (type(user) == SchoolUser):
        return UserSerialiaer(user, many=many)
