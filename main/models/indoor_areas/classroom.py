from django.db import models
from .helpers import inn_dir_path
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
    classroom_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)

    class Meta:
        abstract = True