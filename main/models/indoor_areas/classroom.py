from django.db import models

from main.MyModelFile import MyModel


class Classroom(MyModel):
    total_classroom_count = models.IntegerField(verbose_name="Общее количество учебных/игровых помещений", blank=True,
                                                null=True)

    classroom_ok_count = models.IntegerField(
        verbose_name="Количество учебных/игровых помещений с работоспособным состоянием", blank=True,
        null=True)
    classroom_warning_count = models.IntegerField(
            verbose_name="Количество учебных/игровых помещений с ограниченно работоспособным состоянием", blank=True,
            null=True)
    classroom_emergency_count = models.IntegerField(
            verbose_name="Количество учебных/игровых помещений с аварийным состоянием", blank=True,
            null=True)

    class Meta:
        abstract = True