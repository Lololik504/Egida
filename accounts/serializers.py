from rest_framework.serializers import ModelSerializer
from .models import *
from main.serializers import SchoolsSerializer
from rest_framework import serializers
from .models import MyUser


class UserSerialiaer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['username', 'permission']


