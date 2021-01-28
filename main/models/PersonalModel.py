from django.db import models

from main.MyModelFile import MyModel
from main.models import School


class Personal(MyModel):
    first_name = models.CharField(verbose_name="Имя", max_length=30, default=None, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30, default=None, null=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=30, default=None, null=True)
    phone = models.CharField(verbose_name="Телефон", max_length=30, default=None, null=True)
    email = models.CharField(verbose_name="Email", max_length=50, default=None, null=True)

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"
        app_label = "main"

    def __str__(self):
        ans = ""
        if self.last_name is not None:
            ans += self.last_name
        if self.first_name is not None:
            ans += self.first_name
        if self.patronymic is not None:
            ans += self.patronymic
        if ans == "":
            ans = "-"
        return ans


class Director(Personal):
    school = models.OneToOneField(School, null=True, default=None, on_delete=models.SET_NULL)

    @staticmethod
    def default_director():
        director: Director = Director.objects.create()
        return director

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"
        app_label = "main"


class ZavHoz(Personal):
    school = models.OneToOneField(School, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Завхоз"
        verbose_name_plural = "Завхозы"
        app_label = "main"


class Bookkeeper(Personal):
    school = models.OneToOneField(School, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Бухгалтер"
        verbose_name_plural = "Бухгалтеры"
        app_label = "main"


class Updater(Personal):
    school = models.OneToOneField(School, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Ответственный за заполнение"
        verbose_name_plural = "Ответственные за заполнение"
        app_label = "main"
