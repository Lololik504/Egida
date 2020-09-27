from django.db import models


# Create your models here.

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
# # ----------------For buildings characters-----------------


class BuildingConstructions(models.Model):
    title = models.CharField(max_length=100)


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
    coolent_temp = models.IntegerField()
    air_temp = models.IntegerField()


# -----------------Schools and districts---------------


class District(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, default=None)
    # building_constructions = models.ForeignKey(BuildingConstructions, on_delete=models.CASCADE, default=None, blank=True, null=True)
    # temperatures = models.ForeignKey(Temperatures, on_delete=models.CASCADE, default=None, blank=True, null=True)

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
