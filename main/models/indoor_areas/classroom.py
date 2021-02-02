from django.db import models

from main.MyModelFile import MyModel


class Classroom(MyModel):
    total_classroom_count = models.IntegerField(verbose_name="Общее количество учебных/игровых помещений", blank=True,
                                                null=True)
    classrooms_technical_condition = models.CharField(verbose_name="Техническое состояние учебных помещений",
                                                      max_length=50, null=True, blank=True)
    classroom_count_of_technical_condition_field = models.IntegerField(
        verbose_name="Количество учебных/игровых помещений, относящихся к полю технического состояния", blank=True,
        null=True)

    class Meta:
        abstract = True