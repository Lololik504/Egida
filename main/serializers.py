from rest_framework.serializers import ModelSerializer

from main.models import *


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


class DirectorSerializer(ModelSerializer):
    school = SchoolInfoSerializer

    class Meta:
        model = Director
        fields = ['first_name', 'last_name', 'patronymic', 'school']


class SchoolAllInfoSerializer(ModelSerializer):
    # Сериализация ForeignKey
    district = DistrictsSerializer()

    class Meta:
        model = School
        fields = '__all__'


class BuildingAllInfoSerializer(ModelSerializer):

    class Meta:
        model = Building
        fields = ['__all__']


# class BuildingFieldsSerializer(ModelSerializer)