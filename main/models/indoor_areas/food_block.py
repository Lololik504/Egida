from django.db import models
from .helpers import inn_dir_path
from main.MyModelFile import MyModel


class FoodBlock(MyModel):
    food_block_project_type = models.TextField(verbose_name='Тип пищеблока по проектной документации', null=True,
                                               blank=True)
    food_block_fact_type = models.TextField(verbose_name='Тип фактического использования пищеблока', null=True,
                                            blank=True)
    food_block_building_year = models.IntegerField(verbose_name='Год строительства пищеблока', null=True, blank=True)
    food_block_refactoring_year = models.IntegerField(verbose_name='Год последнего капитального ремонта пищеблока',
                                                      null=True, blank=True)
    food_block_equipment = models.TextField(verbose_name='Требуется ли переоснащение, дооснащение производственного ',
                                            null=True, blank=True)
    food_block_equipment_cost = models.BooleanField(
        verbose_name='Оценочная стоимость переоснащения не проводилась/проводилась', null=True, blank=True)
    food_block_equipment_cost_number = models.FloatField(verbose_name='Оценочная стоимость переоснащения', null=True,
                                                         blank=True)
    food_block_project_seat_count = models.IntegerField(
        verbose_name='Количество посадочных мест в зале приема пищи проектное', null=True, blank=True)
    food_block_fact_seat_count = models.IntegerField(
        verbose_name='Количество посадочных мест в зале приема пищи фактическое', null=True, blank=True)
    food_block_combine_availability = models.BooleanField(verbose_name='Наличие комбината питания', null=True,
                                                          blank=True)
    food_block_combine_count = models.IntegerField(verbose_name='Количество комбинатов питания', null=True, blank=True)
    food_block_dining_availability = models.BooleanField(verbose_name='Наличие школьно-базовых столовых ', null=True,
                                                         blank=True)
    food_block_dining_count = models.IntegerField(verbose_name='Количество школьно-базовых столовых ', null=True,
                                                  blank=True)
    food_block_production_availability = models.BooleanField(
        verbose_name='Наличие производтсва полуфабрикатов и заготовок ', null=True, blank=True)
    food_block_production_count = models.IntegerField(
        verbose_name='Количество производтсва полуфабрикатов и заготовок ', null=True, blank=True)
    food_block_organization_form = models.TextField(verbose_name='Форма организации питания ', null=True, blank=True)
    food_block_technical_condition = models.CharField(verbose_name="Техническое состояние пищеблока",
                                                      max_length=50, null=True, blank=True)
    food_block_exhaust_ventilation = models.BooleanField(verbose_name="Наличие вытяжной вентиляции в пищеблоке",
                                                         null=True, blank=True)
    food_block_exhaust_ventilation_is_workable = models.BooleanField(
        verbose_name="Вытяжная вентиляция в пищеблоке работоспособна", null=True, blank=True)
    food_block_ventilation_type = models.CharField(verbose_name="Тип вентиляции в пищеблоке", max_length=50, null=True,
                                                   blank=True)
    food_block_supply_ventilation = models.BooleanField(verbose_name="Наличие приточной вентиляции в пищеблоке",
                                                        null=True, blank=True)
    food_block_supply_ventilation_is_workable = models.BooleanField(
        verbose_name="Приточная вентиляция в пищеблоке работоспособна", null=True, blank=True)
    food_block_air_heater_type = models.CharField(verbose_name="Тип воздухонагревателя в пищеблоке", max_length=50,
                                                  null=True,
                                                  blank=True)
    food_block_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path,
                                      default=None, null=True, blank=True)

    class Meta:
        abstract = True
