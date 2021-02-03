from django.db import models

from main.MyModelFile import MyModel


class BuildingEntrance(MyModel):
    building_entrance_tactile_mnemonic_diagrams = models.BooleanField(
        verbose_name="Наличие тактильных мнемосхем (Вход в здание)", blank=True, null=True)
    building_entrance_sound_beacons = models.BooleanField(
        verbose_name="Наличие звуковых маяков (кнопка вызова)(Вход в здание)", blank=True, null=True)
    building_entrance_automatic_door_opening = models.BooleanField(
        verbose_name="Наличие функции автоматического открывания дверей (Вход в здание)", blank=True, null=True)
    building_entrance_anti_slip_coating = models.BooleanField(
        verbose_name="Наличие противоскользящего покрытия (Вход в здание)", blank=True, null=True)
    building_entrance_lifts = models.BooleanField(
        verbose_name="Наличие подъемников и лифтов (Вход в здание)", blank=True, null=True)
    building_entrance_ramps = models.BooleanField(
        verbose_name="Наличие пандусов (Вход в здание)", blank=True, null=True)
    building_entrance_handrails_and_railings = models.BooleanField(
        verbose_name="Наличие поручней и перил (Вход в здание)", blank=True, null=True)
    building_entrance_contrast_tape_on_the_steps = models.BooleanField(
        verbose_name="Наличие контрастной ленты на ступенях (Вход в здание)", blank=True, null=True)
    building_entrance_tactile_tiles = models.BooleanField(verbose_name="Наличие тактильной плитки (Вход в здание)",
                                                          blank=True, null=True)
    building_entrance_tactile_information_stand = models.BooleanField(
        verbose_name="Наличие тактильного информационного стенда (Вход в здание)", blank=True, null=True)

    class Meta:
        abstract = True

