from django.db import models

from main.MyModelFile import MyModel


class AdminRoom(MyModel):
    admin_room_total_count = models.IntegerField(verbose_name="Общее количество учебных/игровых помещений", blank=True,
                                                 null=True)
    admin_room_technical_condition = models.CharField(verbose_name="Техническое состояние учебных помещений",
                                                      max_length=50, null=True, blank=True)
    admin_room_ok_status_count = models.IntegerField(
        verbose_name="Количество административных помещений с работоспособным состоянием", blank=True,
        null=True)
    admin_room_warning_status_count = models.IntegerField(
        verbose_name="Количество административных помещений с ограниченно работоспособным состоянием", blank=True,
        null=True)
    admin_room_emergency_status_count = models.IntegerField(
        verbose_name="Количество административных помещений с аварийным состоянием", blank=True,
        null=True)

    class Meta:
        abstract = True
