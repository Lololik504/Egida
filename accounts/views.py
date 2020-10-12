from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser

from .backends import LoginSerializer, MyAuthentication
from .models import *
from .serializers import *
from rest_framework import permissions, status


# Create your views here.


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        token_user = serializer.login(data)
        token = token_user['token']
        user = token_user['user']
        user = UserSerializer(user).data
        ans = {'token': token,
               'user': user}
        return Response(ans, status=status.HTTP_200_OK)


class GetUserByTokenApi(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = MyAuthentication.authenticate(MyAuthentication(), request)
        user = data[0]
        serializer = UserSerializer(user)
        return Response(serializer.data)
