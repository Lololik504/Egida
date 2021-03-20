from django.db import models
from .helpers import inn_dir_path
from main.MyModelFile import MyModel


class Laundry(MyModel):
    laundry_technical_condition = models.CharField(verbose_name="Техническое состояние прачечной",
                                                   max_length=50, null=True, blank=True)
    laundry_exhaust_ventilation = models.BooleanField(verbose_name="Наличие вытяжной вентиляции в прачечной",
                                                      null=True, blank=True)
    laundry_exhaust_ventilation_is_workable = models.BooleanField(
        verbose_name="Вытяжная вентиляция в прачечной работоспособна", null=True, blank=True)
    laundry_ventilation_type = models.CharField(verbose_name="Тип вентиляции в прачечной", max_length=50, null=True,
                                                blank=True)
    laundry_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)

    class Meta:
        abstract = True