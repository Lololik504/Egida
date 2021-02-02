from main.models.safety_system import SafetySystem
from rest_framework.serializers import ModelSerializer


class SafetySystemSerializer(ModelSerializer):
    class Meta:
        model = SafetySystem
        fields = '__all__'
