from django.db import models

from main.MyModelFile import MyModel


class SportsFacilities(MyModel):
    sport_ground_count = models.IntegerField(verbose_name="Количество спортивных площадок", blank=True, null=True)
    sport_ground_ok_count = models.TextField(
        verbose_name="Количество спортивных площадок с работоспособным состоянием", blank=True, null=True)
    sport_ground_warning_count = models.TextField(
        verbose_name="Количество спортивных площадок с ограниченно работоспособным состоянием", blank=True, null=True)
    sport_ground_emergency_count = models.TextField(
        verbose_name="Количество спортивных площадок с аварийным состоянием", blank=True, null=True)

    hockey_rink_count = models.IntegerField(verbose_name="Количество хоккейный коробок", blank=True, null=True)
    hockey_rink_ok_count = models.TextField(
        verbose_name="Количество хоккейных коробок с работоспособным состоянием", blank=True, null=True)
    hockey_rink_warning_count = models.TextField(
        verbose_name="Количество хоккейных коробок с ограниченно работоспособным состоянием", blank=True, null=True)
    hockey_rink_emergency_count = models.TextField(
        verbose_name="Количество хоккейных коробок с аварийным состоянием", blank=True, null=True)

    shade_canopy_count = models.IntegerField(verbose_name="Количество теневых навесов", blank=True, null=True)

    shade_canopy_ok_count = models.TextField(
        verbose_name="Количество теневых навесов с работоспособным состоянием", blank=True, null=True)
    shade_canopy_warning_count = models.TextField(
        verbose_name="Количество теневых навесов с ограниченно работоспособным состоянием", blank=True, null=True)
    shade_canopy_emergency_count = models.TextField(
        verbose_name="Количество теневых навесов с аварийным состоянием", blank=True, null=True)


