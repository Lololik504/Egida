from django.db import models

from main.MyModelFile import MyModel


class Corridor(MyModel):

    corridors_ok_percent = models.FloatField(
        verbose_name="Процент коридоров с работоспособным состоянием", blank=True, null=True)
    corridors_warning_percent = models.FloatField(
            verbose_name="Процент коридоров с ограниченно работоспособным состоянием", blank=True, null=True)
    corridors_emergency_percent = models.FloatField(
            verbose_name="Процент коридоров с аварийным состоянием", blank=True, null=True)

    class Meta:
        abstract = True