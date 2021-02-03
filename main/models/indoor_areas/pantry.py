from django.db import models

from main.MyModelFile import MyModel


class Pantry(MyModel):
    pantry_total_count = models.IntegerField(verbose_name="Общее количество буфетных", blank=True, null=True)

    pantry_ok_count = models.IntegerField(
        verbose_name="Количество буфетных с работоспособным состоянием", blank=True, null=True)
    pantry_warning_count = models.IntegerField(
        verbose_name="Количество буфетных с ограниченно работоспособным состоянием", blank=True, null=True)
    pantry_emergency_count = models.IntegerField(
        verbose_name="Количество буфетных с аварийным состоянием", blank=True, null=True)

    class Meta:
        abstract = True
