from django.db import models

from main.MyModelFile import MyModel


class Pantry(MyModel):
    pantry_total_count = models.IntegerField(verbose_name="Общее количество буфетных", blank=True, null=True)

    pantry_technical_condition = models.CharField(verbose_name="Техническое состояние буфетных",
                                                  max_length=50, null=True, blank=True)
    pantry_count_of_technical_condition_field = models.IntegerField(
        verbose_name="Количество буфетных, относящихся к полю технического состояния", blank=True, null=True)

    class Meta:
        abstract = True