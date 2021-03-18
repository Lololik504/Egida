from django.db import models
from main.MyModelFile import MyModel
from .helpers import inn_dir_path


class Roof(MyModel):

    roof_square = models.FloatField(verbose_name="Площадь кровли", blank=True, null=True)
    roof_type = models.TextField(verbose_name="Тип кровли", null=True, blank=True)
    roof_material = models.TextField(verbose_name="Материал кровли", null=True, blank=True)
    roof_status = models.TextField(verbose_name="Состояние кровли", null=True, blank=True)
    roof_photo = models.FileField(verbose_name="Фото кровли", upload_to=inn_dir_path, default=None, null=True, blank=True)
    roof_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, null=True, blank=True, default=None)

    class Meta:
        abstract = True
