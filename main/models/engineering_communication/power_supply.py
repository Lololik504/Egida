from django.db import models

from main.MyModelFile import MyModel


class PowerSupply(MyModel):
    power_supply_organization = models.CharField(verbose_name="Энергоснабжающая организация", max_length=50, null=True,
                                                 blank=True)
    electric_cable_accessory = models.CharField(verbose_name="Принадлежность электрокабеля", max_length=50, null=True,
                                                blank=True)
    required_power_supply_reliability_category = models.IntegerField(
        verbose_name="Категория надежности электроснабжения (Требуемая)", null=True, blank=True)
    actual_power_supply_reliability_category = models.IntegerField(
        verbose_name="Категория надежности электроснабжения (Фактическая)", null=True, blank=True)
    availability_of_backup_power_supplies = models.CharField(verbose_name="Наличие резервных источников электропитания",
                                                             max_length=50, null=True, blank=True)
    permitted_power = models.IntegerField(verbose_name="Разрешенная мощность", null=True, blank=True)
    ground_loop = models.BooleanField(verbose_name="Наличие контура заземления", null=True, blank=True)
    count_of_energy_saving_lamps_for_indoor_lighting = models.IntegerField(
        verbose_name="Количество энергосберегающих ламп внутреннего освещения", null=True, blank=True)
    count_of_incandescent_lamps_for_indoor_lighting = models.IntegerField(
        verbose_name="Количество ламп накаливания внутреннего освещения", null=True, blank=True)
    count_of_energy_saving_outdoor_lamps = models.IntegerField(
        verbose_name="Количество энергосберегающих ламп наружного освещения", null=True, blank=True)
    count_of_incandescent_outdoor_lamps = models.IntegerField(
        verbose_name="Количество ламп накаливания наружного освещения", null=True, blank=True)
    technical_condition_of_the_internal_power_supply_system = models.CharField(
        verbose_name="Техническое состояние системы внутреннего электроснабжения",
        max_length=50, null=True, blank=True)
    technical_condition_of_the_external_power_supply_system = models.CharField(
        verbose_name="Техническое состояние системы наружного электроснабжения",
        max_length=50, null=True, blank=True)

    class Meta:
        abstract = True
