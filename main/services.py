import json

from django.urls import resolve
from accounts.models import *
from accounts.serializers import *

from accounts.models import SchoolUser


def get_user_class(username):
    try:
        return SchoolUser.objects.get(username=username)
    except:
        pass


def get_user_serialiser(user, many=True):
    if (type(user) == SchoolUser):
        return UserSerialiaer(user, many=many)
