import datetime
from datetime import date
from django.db import models
from django.utils import timezone


# Create your models here.

class District(models.Model):
    name = models.CharField(verbose_name="Район", max_length=50)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name


class School(models.Model):
    INN = models.CharField(verbose_name="ИНН", max_length=13, default='', unique=True)
    name = models.CharField(verbose_name="Полное название", max_length=300, default='', unique=True)
    shortname = models.CharField(verbose_name="Краткое название", max_length=100, default='', unique=True)
    phone = models.CharField(verbose_name="Телефон", max_length=100, default='', unique=True)
    address = models.CharField(verbose_name="Адрес", max_length=300, default='', unique=False)
    district = models.ForeignKey(District, verbose_name="Район", on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"

    def update(self, data):
        self.name = data['name']
        self.shortname = data['shortname']
        self.phone = data['phone']
        self.address = data['address']
        self.district = data['district']
        self.save()

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    patronymic = models.CharField(verbose_name="Отчество", max_length=30)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, default=None)

    class Meta:
        verbose_name = "Директор"
        verbose_name_plural = "Директоры"

    def __str__(self):
        return self.last_name + self.first_name + self.patronymic


class Building(models.Model):

    TYEPS = (
        ()
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=None)
    address = models.CharField(verbose_name="Адрес", max_length=350)

    class TYPE(models.TextChoices):
        FREE_STANDING = "Отдельно стоящее"
        BUILD_INTO_APART = "Встроенное в многоквартирный дом"
        ATTACHED_TO_APART = "Пристроенное к многоквартирному дому"

    type = models.CharField(max_length=50, choices=TYPE.choices)

    class PURPOSE(models.TextChoices):
        FREE_STANDING = "Отдельно стоящее"
        BUILD_INTO_APART = "Встроенное в многоквартирный дом"
        ATTACHED_TO_APART = "Пристроенное к многоквартирному дому"

    purpose = models.CharField(max_length=50, choices=PURPOSE.choices, default=PURPOSE.FREE_STANDING)
    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    construction_year = models.IntegerField(verbose_name="Год", choices=YEAR_CHOICES, default=2000)
    building_square = models.IntegerField(verbose_name="Площадь здания")
    land_square = models.IntegerField(verbose_name="Площадь земельного участка")
    number_of_storeys = models.IntegerField(verbose_name="Этажность")
    build_height = models.IntegerField(verbose_name="Высота здания")
    # build_configure = models.ImageField(verbose_name="Конфигурация здания")
    occupancy_proj = models.IntegerField(verbose_name="Наполняемость проектная")
    occupancy_fact = models.IntegerField(verbose_name="Наполняемость фактическая")
    arend_square = models.IntegerField(verbose_name="Площадь зданий/помещений, сдаваемых в аренду")
    arend_use_type = models.CharField(verbose_name="Вид исспользования", max_length=50)
    unused_square = models.IntegerField(verbose_name="Площадь неиспользуемых зданий/помещений м.кв")
    repair_need_square = models.IntegerField(verbose_name="Площадь, требующая ремонта")

    class TECHNICAL_CONDITION(models.TextChoices):
        WORKING = "Работоспособное"
        LIMITED_WORKING = "Ограниченно-работоспособное"
        EMERGENCY = "Аварийное"

    technical_condition = models.CharField(verbose_name="Техническое состояние", max_length=50,
                                           choices=TECHNICAL_CONDITION.choices)
    last_repair_year = models.IntegerField(verbose_name="Год последнего капитально ремонта", choices=YEAR_CHOICES,
                                           default=2000)


# class Adress(models.Model):
#     street = models.CharField(max_length=50)
#     build_number = models.CharField(max_length=50)
#     school = models.ForeignKey(School, on_delete=models.DO_NOTHING, default=None)
#
#     class Meta:
#         verbose_name = "Адрес"
#         verbose_name_plural = "Адреса"
#
#     def __str__(self):
#         return self.street + self.build_number


# ----------------For Entity-------------------
#
# class RepairWorks(models.Model):
#     title = models.CharField(max_length = 100)
#
#
# class Mandates(models.Model):
#     title = models.CharField(max_length = 100)
#
#
# class DeputiesOrders(models.Model):
#     title = models.CharField(max_length = 100)
#
#
# class Documentation(models.Model):
#     title = models.CharField(max_length = 100)
#
#
# class Entity(models.Model):
#     repair_works = models.ForeignKey(RepairWorks, on_delete=models.CASCADE)
#     mandates = models.ForeignKey(Mandates, on_delete=models.CASCADE)
#     deputies_orders = models.ForeignKey(DeputiesOrders, on_delete=models.CASCADE)
#     documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE)
#     is_municipal = models.BooleanField('Муниципальное здание')
#
#


#  ----------------For buildings characters-----------------


# class EngineeringStructures(models.Model):
#     title = models.CharField(max_length = 100)
#
#
# class IndoorSpaces(models.Model):
#     title = models.CharField(max_length = 100)
#
#
# class SafetySystem(models.Model):
#     title = models.CharField(max_length = 100)
#
#
# class Landscaping(models.Model):
#     title = models.CharField(max_length = 100)
#
#
# class SportsFacilietes(models.Model):
#     title = models.CharField(max_length = 100)
#

class Temperatures(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, default='')
    coolent_temp = models.IntegerField(blank=True, default=15)
    air_temp = models.IntegerField(blank=True, default=15)
    date: date = models.DateField(auto_now=True)

    def __str__(self):
        return self.date
