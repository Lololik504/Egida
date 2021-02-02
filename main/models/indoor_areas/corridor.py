from django.db import models

from main.MyModelFile import MyModel


class Corridor(MyModel):
    corridors_technical_condition = models.CharField(verbose_name="Техническое состояние учебных помещений",
                                                     max_length=50, null=True, blank=True)
    corridors_percent_of_technical_condition_field = models.FloatField(
        verbose_name="Процент коридоров, относящихся к полю технического состояния", blank=True, null=True)

    class Meta:
        abstract = True