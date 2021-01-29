from main.models.building_construction import *
from rest_framework.serializers import ModelSerializer


class BuildingConstructionSerializer(ModelSerializer):
    class Meta:
        model = BuildingConstruction
        fields = '__all__'
