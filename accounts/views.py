from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from rest_framework import permissions, status


# Create your views here.

class UserLogin(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        """
        Try to login a customer (food orderer)
        """
        data = request.data
        try:
            username = data['username']
            password = data['password']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        print(username, password)
        try:
            user = User.objects.get(username=username, password=password)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            user_token = user.auth_token.key
        except:
            user_token = Token.objects.create(user=user)
        user = SchoolUser.objects.get(username=username)
        user_serializer = UserSerialiaer(user, many=False)
        data = {'token': user_token,
                'user': user_serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)

