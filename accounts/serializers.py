from rest_framework.serializers import ModelSerializer
from .models import *
from main.serializers import SchoolsSerializer, DistrictsSerializer
from rest_framework import serializers
from .models import MyUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'permission']


class SchoolUserSerializer(ModelSerializer):
    school = SchoolsSerializer

    class Meta:
        model = SchoolUser
        fields = ['username', 'permission', 'school']


class DistrictUserSerializer(ModelSerializer):
    district = DistrictsSerializer

    class Meta:
        model = DistrictUser
        fields = ['username', 'permission', 'district']
