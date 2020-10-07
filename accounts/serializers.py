from rest_framework.serializers import ModelSerializer
from .models import *
from main.serializers import SchoolsSerializer

class UserSerialiaer(ModelSerializer):
    school = SchoolsSerializer(many=False)
    class Meta:
        model = SchoolUser
        fields = ['username', 'school', 'permission']