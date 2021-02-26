from datetime import datetime

import jwt

from django.conf import settings
from django.contrib.auth import authenticate

from rest_framework import exceptions, serializers, authentication

from .models import MyUser


class MyAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'auth'

    def authenticate(self, request):
        # request.user = None

        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None

        elif len(auth_header) > 2:
            return None
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
        if prefix.lower() != auth_header_prefix:
            return None
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception as e:
            msg = f'Invalid authentication. Could not decode token. {token}     {settings.SECRET_KEY}      {e}'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = MyUser.objects.get(pk=payload['id'])
        except MyUser.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password', 'token',)

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=128, write_only=True)

    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def login(self, data):
        username = data['username']
        password = data['password']
        user = MyUser.authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'token': user.token,
            'user': user
        }
