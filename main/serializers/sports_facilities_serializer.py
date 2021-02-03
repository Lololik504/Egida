from main.models.sports_facilities import SportsFacilities
from rest_framework.serializers import ModelSerializer


class SportsFacilitiesSerializer(ModelSerializer):
    class Meta:
        model = SportsFacilities
        fields = '__all__'
