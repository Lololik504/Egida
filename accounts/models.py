import enum

from django.db import models
from main.models import School
from django.contrib.auth.models import User


# Create your models here.

class Permissions(enum.Enum):
    admin = 1
    departament = 5
    district = 10
    school = 15


class SchoolUser(User):
    #Модель пользователя
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING,default=None)
    permission = models.IntegerField(default=Permissions.school.value)

    class Meta:
        verbose_name = "Пользователь школы"
        verbose_name_plural = "Пользователи школ"

    def __str__(self):
        return self.username




