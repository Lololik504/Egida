from django.db import models
from .helpers import inn_dir_path, inn_dir_path2
from main.MyModelFile import MyModel


class HeatingSystem(MyModel):
    heat_power_supply_organization = models.CharField(verbose_name="Энергоснабжающая организация", max_length=50, null=True,
                                                 blank=True)
    heat_point_type = models.CharField(verbose_name="Тип теплового пункта", max_length=50, null=True,
                                       blank=True)
    ITP_commissioning_year = models.IntegerField(verbose_name="Год ввода в эксплуатацию ИТП", blank=True, null=True)
    year_of_acceptance_on_maintenance = models.IntegerField(verbose_name="Год принятия на баланс или техобслуживание",
                                                            blank=True, null=True)
    heat_supply_source = models.CharField(verbose_name="Источник теплоснабжения", max_length=50, null=True, blank=True)
    heat_powered_by_camera = models.CharField(verbose_name="Питание от камеры №", max_length=50, null=True, blank=True)
    heat_power_supply_from_line = models.CharField(verbose_name="Питание от магистрали №", max_length=50, null=True,
                                              blank=True)
    operational_responsibility_boundary = models.CharField(verbose_name="Граница эксплуатационной ответственности",
                                                           max_length=50, null=True, blank=True)
    hot_water_connection_diagram = models.CharField(verbose_name="Схема подключение горячего водоснабжения",
                                                    max_length=50, null=True, blank=True)
    heating_system_connection_type = models.CharField(verbose_name="Тип присоединения системы отопления ",
                                                      max_length=50, null=True, blank=True)
    Temperature_graph = models.CharField(verbose_name="Температурный график", max_length=50, null=True, blank=True)
    heating_system_wiring_type = models.CharField(verbose_name="Тип разводки системы отопления", max_length=50,
                                                  null=True, blank=True)
    thermal_loads_heating = models.IntegerField(verbose_name="Тепловая нагрузка (Отопление)", null=True, blank=True)
    thermal_loads_hot_water_supply = models.IntegerField(verbose_name="Тепловая нагрузка (Горячее водоснабжение)",
                                                         null=True, blank=True)
    thermal_loads_ventilation = models.IntegerField(verbose_name="Тепловая нагрузка (Вентиляция)", null=True,
                                                    blank=True)
    thermal_loads_total = models.IntegerField(verbose_name="Тепловая нагрузка (Суммарная)", null=True, blank=True)
    number_of_automatic_heat_control_systems = models.IntegerField(
        verbose_name="Количество систем автоматического регулирования тепла", null=True, blank=True)
    number_of_automatic_control_systems_for_the_air_handling_unit = models.IntegerField(
        verbose_name="Количество систем автоматического регулирования приточной установки", null=True, blank=True)
    technical_condition_of_the_heating_system = models.CharField(verbose_name="Техническое состояние системы отопления",
                                                                 max_length=50, null=True, blank=True)
    technical_condition_of_the_ventilation_system = models.CharField(
        verbose_name="Техническое состояние системы вентиляции", max_length=50, null=True, blank=True)
    technical_condition_of_the_hot_water_supply_system = models.CharField(
        verbose_name="Техническое состояние системы горячего водоснабжения", max_length=50, null=True, blank=True)
    technical_condition_of_the_heating_system_act = models.FileField(verbose_name='Акт обследования технического состояния', upload_to=inn_dir_path, default=None, null=True, blank=True)
    technical_condition_of_the_ventilation_system_act = models.FileField(verbose_name='Акт обследования технического состояния', upload_to=inn_dir_path, default=None, null=True, blank=True)
    technical_condition_of_the_hot_water_supply_system_act = models.FileField(verbose_name='Акт обследования технического состояния', upload_to=inn_dir_path, default=None, null=True, blank=True)

    passport_vvoda = models.FileField(verbose_name='Паспорт ввода', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    schema_vvoda = models.FileField(verbose_name='Схема ввода', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    passport_itp = models.FileField(verbose_name='Паспорт ИТП', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    schema_itp = models.FileField(verbose_name='Схема ИТП', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    act_balance_razgranich = models.FileField(verbose_name='Акт балансового разграничения', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    schema_balance_razgranich = models.FileField(verbose_name='Схема балансового разграничения', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    spravka_teplov_nagruz = models.FileField(verbose_name='Справка о тепловых нагрузках', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    raschet_teplov_poter = models.FileField(verbose_name='Расчет тепловых потерь', upload_to=inn_dir_path2, default=None, null=True, blank=True)
    toposnova = models.FileField(verbose_name='Топоснова', upload_to=inn_dir_path2, default=None, null=True, blank=True)

    class Meta:
        abstract = True
