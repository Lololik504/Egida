from django.db import models

from main.MyModelFile import MyModel
from .helpers import inn_dir_path


class Foundation(MyModel):

    foundation_type = models.CharField(verbose_name="Тип фундамента", max_length=50, null=True, blank=True)
    foundation_status = models.CharField(verbose_name="Состояние фундамента", max_length=50, null=True, blank=True)
    foundation_photo = models.FileField(verbose_name="Фото фундамента", upload_to=inn_dir_path, default=None, null=True, blank=True)
    foundation_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)

    class Meta:
        abstract = True