from django.db import models

from main.MyModelFile import MyModel
from .helpers import inn_dir_path


class BlindArea(MyModel):

    blind_area_square = models.FloatField(verbose_name="Площадь отмостки", blank=True, null=True)
    blind_area_length = models.FloatField(verbose_name="Длина отмостки", blank=True, null=True)
    blind_area_type = models.CharField(verbose_name="Тип отмостки", max_length=50, null=True, blank=True)
    blind_area_status = models.CharField(verbose_name="Состояние отмостки", max_length=50, null=True, blank=True)
    blind_area = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)

    class Meta:
        abstract = True
