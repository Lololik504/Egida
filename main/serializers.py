from rest_framework.serializers import ModelSerializer

from main.models import District


class MainSerializer(ModelSerializer):
   class Meta:
       model = District
       fields = ['name']