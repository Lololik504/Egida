from django.db import models
from .helpers import inn_dir_path
from main.MyModelFile import MyModel


class Auditorium(MyModel):
    auditorium_ok_percent = models.FloatField(
        verbose_name="Процент актовых залов с работоспособным состоянием", blank=True, null=True)
    auditorium_warning_percent = models.FloatField(
        verbose_name="Процент актовых залов с ограниченно работоспособным состоянием", blank=True, null=True)
    auditorium_emergency_percent = models.FloatField(
        verbose_name="Процент актовых залов с аварийным состоянием", blank=True, null=True)

    auditorium_exhaust_ventilation = models.BooleanField(verbose_name="Наличие вытяжной вентиляции в актовых залах",
                                                         null=True, blank=True)
    auditorium_exhaust_ventilation_is_workable = models.BooleanField(
        verbose_name="Вытяжная вентиляция в актовых залах работоспособна", null=True, blank=True)
    auditorium_ventilation_type = models.CharField(verbose_name="Тип вентиляции в актовых залах", max_length=50,
                                                   null=True, blank=True)
    auditorium_supply_ventilation = models.BooleanField(verbose_name="Наличие приточной вентиляции в актовых залах",
                                                        null=True, blank=True)

    auditorium_supply_ventilation_is_workable = models.BooleanField(
        verbose_name="Приточная вентиляция в актовых залах работоспособна", null=True, blank=True)
    auditorium_air_heater_type = models.CharField(verbose_name="Тип воздухонагревателя в актовых залах", max_length=50,
                                                  null=True, blank=True)
    auditorium_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)

    class Meta:
        abstract = True
