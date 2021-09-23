from django.db import models

from main.MyModelFile import MyModel


class SurfaceWastewater(MyModel):
    centralized_storm_sewer_system = models.BooleanField(
        verbose_name="Наличие централизованной системы ливневой канализации на территории образовательного учреждения",
        null=True, blank=True)
    the_number_of_wells_of_the_storm_sewer_system = models.IntegerField(
        verbose_name="Количество колодцев системы ливневой канализации на территории учреждения", null=True, blank=True)
    storm_water_inlet = models.BooleanField(
        verbose_name="Наличие дождеприемника на территории учреждения",
        null=True, blank=True)
    number_of_storm_water_inlets = models.IntegerField(
        verbose_name="Количество дождеприемников на территории учреждения", null=True, blank=True)
    water_occurs_onto_low_relief = models.BooleanField(
        verbose_name="Слив дождевой и талой воды происходит самотеком на пониженный рельеф местности",
        null=True, blank=True)

    roof_square = models.FloatField(verbose_name='Площадь кровли', null=True, blank=True)
    paved_square = models.FloatField(verbose_name='Площадь асфальтированной территории', null=True, blank=True)
    ground_square = models.FloatField(verbose_name='Площадь грунтовой поверхности ', null=True, blank=True)
    lawn_square = models.FloatField(verbose_name='Площадь газона', null=True, blank=True)
    rubber_square = models.FloatField(verbose_name='Площадь резинового покрытия', null=True, blank=True)
    all_square = models.FloatField(verbose_name='Общая площадь территории ', null=True, blank=True)

    class Meta:
        abstract = True
