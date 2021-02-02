from django.db import models

from main.MyModelFile import MyModel


class EmergencyExit(MyModel):
    emergency_exit_total_count = models.IntegerField(verbose_name="Общее количество эвакуационных выходов", blank=True,
                                                     null=True)
    emergency_exit_condition = models.CharField(verbose_name="Техническое состояние эвакуационных выходов",
                                                max_length=50, null=True, blank=True)
    emergency_exit_count_of_technical_condition_field = models.IntegerField(
        verbose_name="Количество эвакуационных выходов, относящихся к полю технического состояния", blank=True,
        null=True)
    auto_opening_of_emergency_exits_system = models.BooleanField(
        verbose_name="Наличие системы автоматического открывания эвакуационных выходов", null=True, blank=True)

    class Meta:
        abstract = True