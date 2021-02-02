from django.db import models

from main.MyModelFile import MyModel


class Bathroom(MyModel):
    bathroom_total_count = models.IntegerField(verbose_name="Общее количество санузлов", blank=True, null=True)
    bathroom_technical_condition = models.CharField(verbose_name="Техническое состояние санузлов",
                                                    max_length=50, null=True, blank=True)
    bathroom_count_of_technical_condition_field = models.IntegerField(
        verbose_name="Количество санузлов, относящихся к полю технического состояния", blank=True, null=True)
    bathroom_exhaust_ventilation = models.BooleanField(verbose_name="Наличие вытяжной вентиляции в санузлах",
                                                       null=True, blank=True)
    bathroom_exhaust_ventilation_is_workable = models.BooleanField(
        verbose_name="Вытяжная вентиляция в санузлах работоспособна", null=True, blank=True)
    bathroom_ventilation_type = models.CharField(verbose_name="Тип вентиляции в санузлах", max_length=50, null=True,
                                                 blank=True)

    class Meta:
        abstract = True