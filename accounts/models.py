from datetime import datetime, timedelta

import jwt
from django.contrib.auth.models import AbstractUser, User
from django.db import models

from Egida import settings
from main.models import School, District


# Create your models here.


class MyUser(User):
    class Permissions(models.IntegerChoices):
        ADMIN = 1
        DEPARTAMENT = 5
        DISTRICT = 10
        SCHOOL = 15

    permission = models.IntegerField(null=False, choices=Permissions.choices)

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
    school = models.OneToOneField(School, on_delete=models.CASCADE, default=None, unique=True)

    class Meta:
        verbose_name = "Пользователь школы"
        verbose_name_plural = "Пользователи школ"

    def __str__(self):
        return self.username

    def __init__(self, *args, **kwargs):
        self._meta.get_field('permission').default = MyUser.Permissions.SCHOOL.value
        super(SchoolUser, self).__init__(*args, **kwargs)


class DistrictUser(MyUser):
    # Пользователь района
    district = models.OneToOneField(District, on_delete=models.CASCADE, default=None, unique=True)

    class Meta:
        verbose_name = "Пользователь района"
        verbose_name_plural = "Пользователи района"

    def __str__(self):
        return self.username

    def __init__(self, *args, **kwargs):
        self._meta.get_field('permission').default = MyUser.Permissions.DISTRICT.value
        super(DistrictUser, self).__init__(*args, **kwargs)


class DepartamentUser(MyUser):
    class Meta:
        verbose_name = "Пользователь департамента"
        verbose_name_plural = "Пользователи департамента"

    def __str__(self):
        return self.username

    def __init__(self, *args, **kwargs):
        self._meta.get_field('permission').default = MyUser.Permissions.DEPARTAMENT.value
        super(DepartamentUser, self).__init__(*args, **kwargs)


class AdminUser(MyUser):
    class Meta:
        verbose_name = "Админ сайта"
        verbose_name_plural = "Админы сайта"

    def __str__(self):
        return self.username

    def __init__(self, *args, **kwargs):
        self._meta.get_field('permission').default = MyUser.Permissions.ADMIN.value
        super(AdminUser, self).__init__(*args, **kwargs)
