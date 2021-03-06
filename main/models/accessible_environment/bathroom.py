from django.db import models

from main.MyModelFile import MyModel


class Bathroom(MyModel):
    bathroom_sound_beacons = models.BooleanField(
        verbose_name="Наличие звуковых маяков (кнопка вызова)(Санузел)", blank=True, null=True)
    bathroom_handrails_and_railings = models.BooleanField(
        verbose_name="Наличие поручней и перил (Санузел)", blank=True, null=True)
    bathroom_contrast_tape_on_the_steps = models.BooleanField(
        verbose_name="Наличие контрастной ленты на ступенях (Санузел)", blank=True, null=True)
    bathroom_tactile_tiles = models.BooleanField(verbose_name="Наличие тактильной плитки (Санузел)",
                                                 blank=True, null=True)
    bathroom_tactile_information_stand = models.BooleanField(
        verbose_name="Наличие тактильного информационного стенда (Санузел)", blank=True, null=True)

    class Meta:
        abstract = True
