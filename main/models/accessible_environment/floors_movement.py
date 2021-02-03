from django.db import models

from main.MyModelFile import MyModel


class FloorsMovement(MyModel):
    floors_movement_tactile_mnemonic_diagrams = models.BooleanField(
        verbose_name="Наличие тактильных мнемосхем (Движение по этажам)", blank=True, null=True)
    floors_movement_sound_beacons = models.BooleanField(
        verbose_name="Наличие звуковых маяков (кнопка вызова)(Движение по этажам)", blank=True, null=True)
    floors_movement_automatic_door_opening = models.BooleanField(
        verbose_name="Наличие функции автоматического открывания дверей (Движение по этажам)", blank=True, null=True)
    floors_movement_anti_slip_coating = models.BooleanField(
        verbose_name="Наличие противоскользящего покрытия (Движение по этажам)", blank=True, null=True)
    floors_movement_lifts = models.BooleanField(
        verbose_name="Наличие подъемников и лифтов (Движение по этажам)", blank=True, null=True)
    floors_movement_ramps = models.BooleanField(
        verbose_name="Наличие пандусов (Движение по этажам)", blank=True, null=True)
    floors_movement_handrails_and_railings = models.BooleanField(
        verbose_name="Наличие поручней и перил (Движение по этажам)", blank=True, null=True)
    floors_movement_contrast_tape_on_the_steps = models.BooleanField(
        verbose_name="Наличие контрастной ленты на ступенях (Движение по этажам)", blank=True, null=True)
    floors_movement_tactile_tiles = models.BooleanField(verbose_name="Наличие тактильной плитки (Движение по этажам)",
                                                        blank=True, null=True)
    floors_movement_tactile_information_stand = models.BooleanField(
        verbose_name="Наличие тактильного информационного стенда (Движение по этажам)", blank=True, null=True)

    class Meta:
        abstract = True

