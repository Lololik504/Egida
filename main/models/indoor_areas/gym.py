from django.db import models

from main.MyModelFile import MyModel


class Gym(MyModel):
    gym_room_total_count = models.IntegerField(verbose_name="Общее количество спортзалов", blank=True, null=True)

    gym_ok_percent = models.FloatField(
        verbose_name="Процент спортзалов с работоспособным состоянием", blank=True, null=True)
    gym_warning_percent = models.FloatField(
        verbose_name="Процент спортзалов с ограниченно работоспособным состоянием", blank=True, null=True)
    gym_emergency_percent = models.FloatField(
        verbose_name="Процент спортзалов с аварийным состоянием", blank=True, null=True)

    gym_exhaust_ventilation = models.BooleanField(verbose_name="Наличие вытяжной вентиляции в спортзалах",
                                                  null=True, blank=True)
    gym_exhaust_ventilation_is_workable = models.BooleanField(
        verbose_name="Вытяжная вентиляция в спортзалах работоспособна", null=True, blank=True)
    gym_ventilation_type = models.CharField(verbose_name="Тип вентиляции в спортзалах", max_length=50, null=True,
                                            blank=True)
    gym_supply_ventilation = models.BooleanField(verbose_name="Наличие приточной вентиляции в спортзалах",
                                                 null=True, blank=True)
    gym_supply_ventilation_is_workable = models.BooleanField(
        verbose_name="Приточная вентиляция в спортзалах работоспособна", null=True, blank=True)
    gym_air_heater_type = models.CharField(verbose_name="Тип воздухонагревателя в спортзалах", max_length=50, null=True,
                                           blank=True)

    class Meta:
        abstract = True