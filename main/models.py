from datetime import date
from .translit import latinizator
from django.db import models
from django.utils import timezone


# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name


class School(models.Model):
    INN = models.CharField(max_length=13, default='', unique=True)
    name = models.CharField(max_length=300, default='', unique=True)
    shortname = models.CharField(max_length=100, default='', unique=True)
    phone = models.CharField(max_length=100, default='', unique=True)
    adress = models.CharField(max_length=300, default='', unique=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE, default=None)

    #     engineering_structures = models.ForeignKey(EngineeringStructures, on_delete=models.CASCADE)
    #     indoor_spaces = models.ForeignKey(IndoorSpaces, on_delete=models.CASCADE)
    #     safety_system = models.ForeignKey(SafetySystem, on_delete=models.CASCADE)
    #     landscaping = models.ForeignKey(Landscaping, on_delete=models.CASCADE)
    #     sports_facilietes = models.ForeignKey(SportsFacilietes, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, default=None)

    class Meta:
        verbose_name = "Директор"
        verbose_name_plural = "Директоры"

    def __str__(self):
        return self.last_name + self.first_name + self.patronymic


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
