from django.db import models

from main.MyModelFile import MyModel


class WaterSupply(MyModel):
    water_supply_organization = models.CharField(verbose_name="Водоснабжающая организация", max_length=50, null=True,
                                                 blank=True)
    technical_condition_of_the_water_supply_system = models.CharField(
        verbose_name="Техническое состояние системы водоснабжения", max_length=50, null=True, blank=True)
    technical_condition_of_the_sewerage_system = models.CharField(
        verbose_name="Техническое состояние системы канализирования", max_length=50, null=True, blank=True)

    class Meta:
        abstract = True
