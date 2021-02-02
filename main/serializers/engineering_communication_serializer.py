from main.models.engineering_communication import *
from rest_framework.serializers import ModelSerializer


class EngineeringCommunicationSerializer(ModelSerializer):
    class Meta:
        model = EngineeringCommunication
        fields = '__all__'
