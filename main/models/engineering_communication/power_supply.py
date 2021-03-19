from django.db import models
from .helpers import inn_dir_path, inn_dir_path2
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
    technical_condition_of_the_internal_power_supply_system_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)
    technical_condition_of_the_external_power_supply_system_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)
    power_supply_system_act_balance_razgranich = models.FileField(verbose_name='Акт балансового разграничения', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    power_supply_system_scheme_balance_razgranich = models.FileField(verbose_name='Схема балансового разграничения', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    power_supply_system_odnolinein_schema = models.FileField(verbose_name='Однолинейная схема', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    power_supply_system_photo_vru = models.FileField(verbose_name='Фото ВРУ', upload_to=inn_dir_path2, default=None, null=True, blank=True)

    
    class Meta:
        abstract = True
