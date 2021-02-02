from django.db import models

from main.MyModelFile import MyModel


class Roof(MyModel):
    roof_square = models.FloatField(verbose_name="Площадь кровли", blank=True, null=True)
    roof_type = models.CharField(verbose_name="Тип кровли", max_length=50, null=True, blank=True)
    roof_material = models.CharField(verbose_name="Материал кровли", max_length=50, null=True, blank=True)
    roof_status = models.CharField(verbose_name="Состояние кровли", max_length=50, null=True, blank=True)

    class Meta:
        abstract = True
