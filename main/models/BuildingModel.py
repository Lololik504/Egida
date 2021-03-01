# Create your models here.
import datetime
from annoying.fields import AutoOneToOneField

from django.db import models

from main.MyModelFile import MyModel

from main.models.accessible_environment import AccessibleEnvironment
from main.models.building_construction import BuildingConstruction
from main.models.engineering_communication import EngineeringCommunication
from main.models.indoor_areas import IndoorAreas
from main.models.safety_system import SafetySystem
from main.models.sports_facilities import SportsFacilities
from main.models.territory_improvement import TerritoryImprovement


class Building(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    street = models.CharField(verbose_name="Улица", max_length=300, blank=True, null=True)
    street_number = models.CharField(verbose_name="Номер дома", max_length=50, blank=True, null=True)

    class TYPE(models.TextChoices):
        FREE_STANDING = "Отдельно стоящее"
        BUILD_INTO_APART = "Встроенное в многоквартирный дом"
        ATTACHED_TO_APART = "Пристроенное к многоквартирному дому"

    type = models.CharField(verbose_name="Вид здания", max_length=50, choices=TYPE.choices, default=TYPE.FREE_STANDING,
                            blank=True, null=True)

    purpose = models.CharField(verbose_name="Назначение здания", max_length=200, blank=True,
                               null=True)

    YEAR_CHOICES = []
    YEAR_CHOICES_FOR_RESPONSE = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
        YEAR_CHOICES_FOR_RESPONSE.append(r)

    construction_year = models.IntegerField(verbose_name="Год постройки здания", choices=YEAR_CHOICES, default=2000,
                                            blank=True,
                                            null=True)
    building_square = models.FloatField(verbose_name="Площадь здания", blank=True, null=True)
    land_square = models.FloatField(verbose_name="Площадь земельного участка", blank=True, null=True)
    number_of_storeys = models.IntegerField(verbose_name="Этажность", blank=True, null=True)
    build_height = models.FloatField(verbose_name="Высота здания", blank=True, null=True)
    # build_configure = models.ImageField(verbose_name="Конфигурация здания")
    occupancy_proj = models.IntegerField(verbose_name="Наполняемость проектная", blank=True, null=True)
    occupancy_fact = models.IntegerField(verbose_name="Наполняемость фактическая", blank=True, null=True)
    arend_square = models.FloatField(verbose_name="Площадь зданий/помещений, сдаваемых в аренду", blank=True,
                                       null=True)
    arend_use_type = models.CharField(verbose_name="Вид исспользования", max_length=50, blank=True, null=True)
    unused_square = models.FloatField(verbose_name="Площадь неиспользуемых зданий/помещений м.кв", blank=True,
                                        null=True)
    repair_need_square = models.FloatField(verbose_name="Площадь, требующая ремонта", blank=True, null=True)

    class TECHNICAL_CONDITION(models.TextChoices):
        WORKING = "Работоспособное"
        LIMITED_WORKING = "Ограниченно-работоспособное"
        EMERGENCY = "Аварийное"

    technical_condition = models.CharField(verbose_name="Техническое состояние", max_length=50,
                                           choices=TECHNICAL_CONDITION.choices, blank=True, null=True)
    last_repair_year = models.IntegerField(verbose_name="Год последнего капитально ремонта", choices=YEAR_CHOICES,
                                           default=2000, blank=True, null=True)

    #################################
    building_construction = AutoOneToOneField(BuildingConstruction, verbose_name="Строительные конструкции",
                                              on_delete=models.CASCADE, default=None, null=True, blank=True)
    #################################
    engineering_communication = AutoOneToOneField(EngineeringCommunication, verbose_name="Инженерные коммуникации",
                                                  on_delete=models.CASCADE, default=None, null=True, blank=True)
    #################################
    indoor_areas = AutoOneToOneField(IndoorAreas, verbose_name="Внутренние помещения",
                                     on_delete=models.CASCADE, default=None, null=True, blank=True)
    #################################
    safety_system = AutoOneToOneField(SafetySystem, verbose_name="Система безопасности",
                                      on_delete=models.CASCADE, default=None, null=True, blank=True)
    #################################
    territory_improvement = AutoOneToOneField(TerritoryImprovement, verbose_name="Система безопасности",
                                              on_delete=models.CASCADE, default=None, null=True, blank=True)
    #################################
    sports_facilities = AutoOneToOneField(SportsFacilities, verbose_name="Спортивные сооружения",
                                          on_delete=models.CASCADE, default=None, null=True, blank=True)
    #################################
    accessible_environment = AutoOneToOneField(AccessibleEnvironment, verbose_name="Спортивные сооружения",
                                               on_delete=models.CASCADE, default=None, null=True, blank=True)
    #################################

    def get_choices(self):
        res = {
            'TYPE': self.TYPE.values,
            # 'PURPOSE': self.PURPOSE.values,
            'YEAR_CHOICES': self.YEAR_CHOICES_FOR_RESPONSE,
            'TECHNICAL_CONDITION': self.TECHNICAL_CONDITION.values
        }
        return res

    def __str__(self):
        if self.street is None:
            return "-"
        if self.street_number is None:
            return self.street
        return self.street + self.street_number

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"
        app_label = "main"
