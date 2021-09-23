from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import *


class DistrictsNameSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ['name', ]


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
        # fields = '__all__'
        exclude = ('building_construction', 'engineering_communication', 'indoor_areas')


class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = ['id', 'street', 'street_number']


class TemperatureSerializer(ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'


class RequisitesSerializer(ModelSerializer):
    district = DistrictsNameSerializer()

    class Meta:
        model = Requisites
        fields = '__all__'


class DocumentsSerializer(ModelSerializer):
    class Meta:
        encoder = 'ascii'
        model = Document
        fields = ['passport_BTI',
                  'topographic_plan',
                  'teplosnabj_MK',
                  'vodosnabj_MK',
                  'electrosnabj_MK']


class RospotrebSerializer(ModelSerializer):
    class Meta:
        encoder = 'ascii'
        model = Rospotreb
        fields = '__all__'


class GospozhSerializer(ModelSerializer):
    class Meta:
        encoder = 'ascii'
        model = Gospozh
        fields = '__all__'


class RostechSerializer(ModelSerializer):
    class Meta:
        encoder = 'ascii'
        model = Rostech
        fields = '__all__'


class SudebSerializer(ModelSerializer):
    class Meta:
        encoder = 'ascii'
        model = Sudeb
        fields = '__all__'


class OtherOrdersSerializer(ModelSerializer):
    class Meta:
        encoder = 'ascii'
        model = OtherOrders
        fields = '__all__'

class MandateCouncilSerializer(ModelSerializer):
    class Meta:
        encoder = 'ascii'
        model = MandateCouncil
        fields = '__all__'

class MandateAssemblySerializer(ModelSerializer):
    class Meta:
        encoder = 'ascii'
        model = MandateAssembly
        fields = '__all__'

class ZPPPSerializer(ModelSerializer):
    class Meta:
        encoder = 'ascii'
        model = ZPPP
        fields = '__all__'