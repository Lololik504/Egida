from django.db import models

from main.MyModelFile import MyModel


class Window(MyModel):
    window_material = models.CharField(verbose_name="Материал окон", max_length=50, null=True, blank=True)
    energy_saving_window_percent = models.FloatField(verbose_name="Процент энерго-сберегающих окон", blank=True, null=True)
    window_count = models.IntegerField(verbose_name="Количество окон", blank=True, null=True)
    window_square = models.FloatField(verbose_name="Площадь окон", blank=True, null=True)
    window_status = models.CharField(verbose_name="Состояние окон", max_length=50, null=True, blank=True)

    class Meta:
        abstract = True
