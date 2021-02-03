from django.db import models

from main.MyModelFile import MyModel


class TerritoryImprovement(MyModel):
    green_area_square = models.FloatField(verbose_name="Площадь зеленых насаждений", blank=True, null=True)
    emergency_trees_count = models.IntegerField(
        verbose_name="Количество аварийных деревьев, согласно порубочного талона", blank=True, null=True)
    #########################################
    asphalt_area = models.FloatField(verbose_name="Площадь асфальтового покрытия", blank=True, null=True)

    asphalt_ok_percent = models.IntegerField(
        verbose_name="Процент асфальтового покрытия с работоспособным состоянием", blank=True,
        null=True)
    asphalt_warning_percent = models.IntegerField(
        verbose_name="Процент асфальтового покрытия с ограниченно работоспособным состоянием", blank=True,
        null=True)
    asphalt_emergency_percent = models.IntegerField(
        verbose_name="Процент асфальтового покрытия с аварийным состоянием", blank=True,
        null=True)

    #########################################
    fence_volume = models.FloatField(verbose_name="Объем ограждения", blank=True, null=True)

    fence_ok_volume = models.IntegerField(
        verbose_name="Обьём ограждения с работоспособным состоянием", blank=True, null=True)
    fence_warning_volume = models.IntegerField(
        verbose_name="Обьём ограждения с ограниченно работоспособным состоянием", blank=True, null=True)
    fence_emergency_volume = models.IntegerField(
        verbose_name="Обьём ограждения с аварийным состоянием", blank=True, null=True)

    #########################################
    container_site = models.BooleanField(verbose_name="Наличие контейнерной площадки", blank=True, null=True)
    container_site_material = models.TextField(verbose_name="Материал покрытия контейнерной площадки", blank=True,
                                               null=True)
    container_site_square = models.FloatField(verbose_name="Площадь контейнерной площадки", blank=True, null=True)
    container_site_fence = models.BooleanField(verbose_name="Наличие ограждения контейнерной площадки", blank=True,
                                               null=True)
    total_container_volume = models.FloatField(verbose_name="Суммарный объем контейнеров", blank=True, null=True)

    class Meta:
        verbose_name = "Благоустройство территории"
    