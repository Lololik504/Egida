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
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            user = User.objects.get(username=username, password=password)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            user_token = user.auth_token.key
        except:
            Token.objects.create(user=user)
            user_token = user.auth_token.key
        user = MyUser.objects.get(username=username)
        user_serializer = UserSerialiaer(user, many=False)
        data = {'token': user_token,
                'user': user_serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are0 required.
        Returns a JSON web token.
        """
        data = request.data
        print(data)
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        ask = serializer.login(data)

        return Response(ask, status=status.HTTP_200_OK)


class GetUserByTokenApi(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = MyAuthentication.authenticate(MyAuthentication(), request)
        user = data[0]
        serializer = UserSerialiaer(user)
        return Response(serializer.data)
