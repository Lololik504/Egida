from django.db import models
from .helpers import inn_dir_path
from main.MyModelFile import MyModel


class Pantry(MyModel):
    pantry_total_count = models.IntegerField(verbose_name="Общее количество буфетных", blank=True, null=True)

    pantry_ok_count = models.IntegerField(
        verbose_name="Количество буфетных с работоспособным состоянием", blank=True, null=True)
    pantry_warning_count = models.IntegerField(
        verbose_name="Количество буфетных с ограниченно работоспособным состоянием", blank=True, null=True)
    pantry_emergency_count = models.IntegerField(
        verbose_name="Количество буфетных с аварийным состоянием", blank=True, null=True)
    pantry_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)

    class Meta:
        abstract = True
