from django.db import models

from main.MyModelFile import MyModel


class Foundation(MyModel):
    foundation_type = models.CharField(verbose_name="Тип фундамента", max_length=50, null=True, blank=True)
    foundation_status = models.CharField(verbose_name="Состояние фундамента", max_length=50, null=True, blank=True)

    class Meta:
        abstract = True