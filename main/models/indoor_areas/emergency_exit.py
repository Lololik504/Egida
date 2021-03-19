from django.db import models
from .helpers import inn_dir_path
from main.MyModelFile import MyModel


class EmergencyExit(MyModel):
    emergency_exit_total_count = models.IntegerField(verbose_name="Общее количество эвакуационных выходов", blank=True,
                                                     null=True)

    emergency_exit_ok_count = models.IntegerField(
        verbose_name="Количество эвакуационных выходов с работоспособным состоянием", blank=True,
        null=True)
    emergency_exit_warning_count = models.IntegerField(
        verbose_name="Количество эвакуационных выходов с ограниченно работоспособным состоянием", blank=True,
        null=True)
    emergency_exit_emergency_count = models.IntegerField(
        verbose_name="Количество эвакуационных выходов с аварийным состоянием", blank=True,
        null=True)

    auto_opening_of_emergency_exits_system = models.BooleanField(
        verbose_name="Наличие системы автоматического открывания эвакуационных выходов", null=True, blank=True)

    emergency_exit_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)

    class Meta:
        abstract = True