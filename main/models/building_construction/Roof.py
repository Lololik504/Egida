from django.db import models

from main.MyModelFile import MyModel


class Roof(MyModel):
    roof_square = models.FloatField(verbose_name="Площадь кровли", blank=True, null=True)
    roof_type = models.TextField(verbose_name="Тип кровли", null=True, blank=True)
    roof_material = models.TextField(verbose_name="Материал кровли", null=True, blank=True)
    roof_status = models.TextField(verbose_name="Состояние кровли", null=True, blank=True)

    class Meta:
        abstract = True
