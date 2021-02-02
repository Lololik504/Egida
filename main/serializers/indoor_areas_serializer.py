from main.models.indoor_areas import IndoorAreas
from rest_framework.serializers import ModelSerializer


class IndoorAreasSerializer(ModelSerializer):
    class Meta:
        model = IndoorAreas
        fields = '__all__'
