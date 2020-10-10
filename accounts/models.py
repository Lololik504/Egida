import enum
from datetime import datetime, timedelta
import jwt
from django.db import models

from Egida import settings
from main.models import School, District
from django.contrib.auth.models import AbstractUser, User


# Create your models here.

class Permissions(enum.Enum):
    admin = 1
    departament = 5
    district = 10
    school = 15


class MyUser(User):
    permission = models.IntegerField(null=False)

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(minutes=15)

        token = jwt.encode({
            'id': self.pk,
            'pass': self.password
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    @classmethod
    def authenticate(cls, username, password):
        user = MyUser.objects.get(username=username, password=password)
        return user


class SchoolUser(MyUser):
    # Модель пользователя школы
    school = models.OneToOneField(School, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Пользователь школы"
        verbose_name_plural = "Пользователи школ"

    def create(self, **kwargs):
        pass

    def __str__(self):
        return self.username


class DistrictUser(MyUser):
    # Пользователь района
    district = models.OneToOneField(District, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Пользователь района"
        verbose_name_plural = "Пользователи района"

    def __str__(self):
        return self.username


class DepartamentUser(MyUser):
    class Meta:
        verbose_name = "Пользователь департамента"
        verbose_name_plural = "Пользователи департамента"

    def __str__(self):
        return self.username


class AdminUser(MyUser):
    class Meta:
        verbose_name = "Админ сайта"
        verbose_name_plural = "Админы сайта"

    def __str__(self):
        return self.username
