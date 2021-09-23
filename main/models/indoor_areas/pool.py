from django.db import models
from .helpers import inn_dir_path
from main.MyModelFile import MyModel


class Pool(MyModel):
    pool_available = models.BooleanField(verbose_name='Наличие бассейна', null=True, blank=True)
    pool_working = models.BooleanField(verbose_name='Работоспособность бассейна', null=True, blank=True)
    pool_hours_in_day = models.IntegerField(verbose_name='Количество часов в день', null=True, blank=True)
    pool_days_in_week = models.IntegerField(verbose_name='Количество дней в неделю', null=True, blank=True)
    pool_people_in_day = models.IntegerField(verbose_name='Количество человек в день', null=True, blank=True)
    pool_bowl_condition = models.TextField(verbose_name='Состояние чаши бассейна', null=True, blank=True)
    pool_bowl_length = models.FloatField(verbose_name='Длина чаши бассейна', null=True, blank=True)
    pool_bowl_width = models.FloatField(verbose_name='Ширина чаши бассейна', null=True, blank=True)
    pool_bowl_depth = models.FloatField(verbose_name='Глубина чаши бассейна', null=True, blank=True)
    nature_of_water_exchange = models.TextField(verbose_name='Характер водообмена', null=True, blank=True)
    filtration_unit = models.BooleanField(verbose_name='Наличие фильтровальной установки', null=True, blank=True)
    filtration_unit_year = models.IntegerField(verbose_name='Год ввода в эксплуатацию фильтровальной установки',
                                               null=True, blank=True)
    filtration_unit_organization = models.TextField(verbose_name='Организация обслуживающая фильтровальную установку',
                                                    null=True, blank=True)
    pool_bowl_schedule = models.TextField(verbose_name='Режим наполнения чаши бассейна', null=True, blank=True)
    heating_system_condition = models.TextField(verbose_name='Состояние системы отопления в помещении бассейна',
                                                null=True, blank=True)
    heating_lines_system_condition = models.TextField(
        verbose_name='Состояние системы обогрева дорожек в помещении бассейна', null=True, blank=True)
    ventilation_system_condition = models.TextField(verbose_name='Состояние системы вентиляции в помещении бассейна',
                                                    null=True, blank=True)

    class Meta:
        abstract = True
