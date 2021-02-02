from django.db import models

from main.MyModelFile import MyModel


class FoodBlock(MyModel):
    food_block_technical_condition = models.CharField(verbose_name="Техническое состояние учебных помещений",
                                                      max_length=50, null=True, blank=True)
    exhaust_ventilation = models.BooleanField(verbose_name="Наличие вытяжной вентиляции", null=True, blank=True)
    exhaust_ventilation_is_workable = models.BooleanField(verbose_name="Вытяжная вентиляция работоспособна", null=True,
                                                          blank=True)
    ventilation_type = models.CharField(verbose_name="Тип вентиляции", max_length=50, null=True, blank=True)
    supply_ventilation = models.BooleanField(verbose_name="Наличие приточной вентиляции", null=True, blank=True)
    supply_ventilation_is_workable = models.BooleanField(verbose_name="Вытяжная вентиляция работоспособна", null=True,
                                                         blank=True)
    air_heater_type = models.CharField(verbose_name="Тип воздухонагревателя", max_length=50, null=True, blank=True)
    #TODO: Начать писать класс для спортзала
