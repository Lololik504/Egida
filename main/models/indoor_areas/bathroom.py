from django.db import models
from .helpers import inn_dir_path
from main.MyModelFile import MyModel


class Bathroom(MyModel):
    bathroom_total_count = models.IntegerField(verbose_name="Общее количество санузлов", blank=True, null=True)

    bathroom_ok_count = models.IntegerField(
        verbose_name="Количество санузлов с работоспособным состоянием", blank=True, null=True)
    bathroom_warning_count = models.IntegerField(
        verbose_name="Количество санузлов с ограниченно работоспособным состоянием", blank=True, null=True)
    bathroom_emergency_count = models.IntegerField(
        verbose_name="Количество санузлов с аварийным состоянием", blank=True, null=True)
    bathroom_exhaust_ventilation = models.BooleanField(verbose_name="Наличие вытяжной вентиляции в санузлах",
                                                       null=True, blank=True)
    bathroom_exhaust_ventilation_is_workable = models.BooleanField(
        verbose_name="Вытяжная вентиляция в санузлах работоспособна", null=True, blank=True)
    bathroom_ventilation_type = models.CharField(verbose_name="Тип вентиляции в санузлах", max_length=50, null=True,
                                                 blank=True)
    bathroom_act = models.FileField(verbose_name="Акт обследования технического состояния", upload_to=inn_dir_path, default=None, null=True, blank=True)

    class Meta:
        abstract = True
