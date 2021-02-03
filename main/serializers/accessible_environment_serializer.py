from main.models.accessible_environment import AccessibleEnvironment
from rest_framework.serializers import ModelSerializer


class AccessibleEnvironmentSerializer(ModelSerializer):
    class Meta:
        model = AccessibleEnvironment
        fields = '__all__'
