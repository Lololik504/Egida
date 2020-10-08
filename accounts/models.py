import enum
from datetime import datetime, timedelta
import jwt
from django.db import models

from Egida import settings
from accounts.managers import MyUserManager
from main.models import School
from django.contrib.auth.models import AbstractUser, User


# Create your models here.

class Permissions(enum.Enum):
    admin = 1
    departament = 5
    district = 10
    school = 15


class MyUser(User):
    """
    Определяет наш пользовательский класс User.
    Требуется имя пользователя, адрес электронной почты и пароль.
    """

    permission = models.IntegerField(default=Permissions.school.value)

    objects = MyUserManager()

    def __str__(self):
        """
        Возвращает строковое представление этого `User`.
        Эта строка используется, когда в консоли выводится `User`.
        """
        return self.username

    @property
    def token(self):
        """
        Позволяет нам получить токен пользователя, вызвав `user.token` вместо
        `user.generate_jwt_token().

        Декоратор `@property` выше делает это возможным.
        `token` называется «динамическим свойством ».
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей,
        как обработка электронной почты.
        Обычно это имя и фамилия пользователя.
        Поскольку мы не храним настоящее имя пользователя,
        мы возвращаем его имя пользователя.
        """
        return self.username

    def get_short_name(self):
        """
        Этот метод требуется Django для таких вещей,
        как обработка электронной почты.
        Как правило, это будет имя пользователя.
        Поскольку мы не храним настоящее имя пользователя,
        мы возвращаем его имя пользователя.
        """
        return self.username

    def _generate_jwt_token(self):

        dt = datetime.now() + timedelta(days=60)

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
    # Модель пользователя
    school = models.OneToOneField(School, on_delete=models.CASCADE, default=None)
    # REQUIRED_FIELDS = (['school'])

    class Meta:
        verbose_name = "Пользователь школы"
        verbose_name_plural = "Пользователи школ"

    def __str__(self):
        return self.username
