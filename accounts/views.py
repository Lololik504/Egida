from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import permissions

# Create your views here.

class Users(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny]

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerialiaer(users, many=True)
        return Response(serializer.data)

