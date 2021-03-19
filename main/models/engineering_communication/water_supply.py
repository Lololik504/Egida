from django.db import models
from .helpers import inn_dir_path, inn_dir_path2
from main.MyModelFile import MyModel


class WaterSupply(MyModel):
    water_supply_organization = models.CharField(verbose_name="Водоснабжающая организация", max_length=50, null=True,
                                                 blank=True)
    technical_condition_of_the_water_supply_system = models.CharField(
        verbose_name="Техническое состояние системы водоснабжения", max_length=50, null=True, blank=True)
    technical_condition_of_the_sewerage_system = models.CharField(
        verbose_name="Техническое состояние системы канализирования", max_length=50, null=True, blank=True)
    technical_condition_of_the_water_supply_system_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)
    technical_condition_of_the_sewerage_system_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)
    water_supply_scheme_balance_razgranich = models.FileField(verbose_name="Схема балансового разграничения", upload_to=inn_dir_path2, default=None, null=True, blank=True)

    class Meta:
        abstract = True
