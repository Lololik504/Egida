from django.db import models

from main.MyModelFile import MyModel


class StreetTerritory(MyModel):
    markings_and_parking_for_disabled_people = models.BooleanField(
        verbose_name="Наличие разметки и знака парковки для инвалидов", blank=True, null=True)

    street_tactile_tiles = models.BooleanField(verbose_name="Наличие тактильной плитки (Уличная территория)", blank=True, null=True)

    asphalted_area_with_slopes = models.BooleanField(
        verbose_name="Наличие асфальтируемой территории с низким бордюрам и спуском", blank=True, null=True)

    street_tactile_mnemonic_diagrams = models.BooleanField(
        verbose_name="Наличие тактильных мнемосхем (Уличная территория)", blank=True, null=True)

    street_sound_beacons = models.BooleanField(
        verbose_name="Наличие звуковых маяков (кнопка вызова)(Уличная территория)", blank=True, null=True)

    playgrounds_for_children_with_disabilities = models.BooleanField(
        verbose_name="Наличие игровых площадок для детей с ограниченными возможностями", blank=True, null=True)

    induction_system_for_hearing_impaired = models.BooleanField(
        verbose_name="Наличие индукционных систем для слабослышащих", blank=True, null=True)

    class Meta:
        abstract = True

