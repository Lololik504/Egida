from django.db import models
from .helpers import inn_dir_path
from main.MyModelFile import MyModel


class FoodBlock(MyModel):
    food_block_technical_condition = models.CharField(verbose_name="Техническое состояние пищеблока",
                                                      max_length=50, null=True, blank=True)
    food_block_exhaust_ventilation = models.BooleanField(verbose_name="Наличие вытяжной вентиляции в пищеблоке",
                                                         null=True, blank=True)
    food_block_exhaust_ventilation_is_workable = models.BooleanField(
        verbose_name="Вытяжная вентиляция в пищеблоке работоспособна", null=True, blank=True)
    food_block_ventilation_type = models.CharField(verbose_name="Тип вентиляции в пищеблоке", max_length=50, null=True,
                                                   blank=True)
    food_block_supply_ventilation = models.BooleanField(verbose_name="Наличие приточной вентиляции в пищеблоке",
                                                        null=True, blank=True)
    food_block_supply_ventilation_is_workable = models.BooleanField(
        verbose_name="Приточная вентиляция в пищеблоке работоспособна", null=True, blank=True)
    food_block_air_heater_type = models.CharField(verbose_name="Тип воздухонагревателя в пищеблоке", max_length=50, null=True,
                                                  blank=True)
    food_block_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)
    class Meta:
        abstract = True
