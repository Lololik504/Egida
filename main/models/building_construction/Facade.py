from django.db import models

from main.MyModelFile import MyModel


class Facade(MyModel):
    facade_square = models.FloatField(verbose_name="Площадь фасада", blank=True, null=True)
    facade_type = models.CharField(verbose_name="Тип фасада", max_length=50, null=True, blank=True)
    facade_status = models.CharField(verbose_name="Состояние фасада", max_length=50, null=True, blank=True)

    class Meta:
        abstract = True
