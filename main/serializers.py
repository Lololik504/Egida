from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import *


class DistrictsNameSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ['name',]


class DistrictsSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name']


class SchoolInfoSerializer(ModelSerializer):
    # Сериализация ForeignKey
    district = DistrictsSerializer()

    class Meta:
        model = School
        fields = ['INN', 'shortname', 'district']


class PersonalAllInfoSerializer(ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'


class SchoolAllInfoSerializer(ModelSerializer):
    # Сериализация ForeignKey
    district = serializers.CharField(source='district.name', read_only=True)

    class Meta:
        model = School
        fields = "__all__"


class BuildingAllInfoSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = ['id', 'street', 'street_number']


class TemperatureSerializer(ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'
