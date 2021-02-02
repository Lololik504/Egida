from main.models.territory_improvement import TerritoryImprovement
from rest_framework.serializers import ModelSerializer


class TerritoryImprovementSerializer(ModelSerializer):
    class Meta:
        model = TerritoryImprovement
        fields = '__all__'
