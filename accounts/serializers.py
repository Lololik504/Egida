from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerialiaer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]