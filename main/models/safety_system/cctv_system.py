from django.db import models

from main.MyModelFile import MyModel


class CCTV(MyModel):  # Closed Circuit Television
    CCTV_installation_year = models.IntegerField(verbose_name="Год установки системы видеонаблюдения", blank=True,
                                                 null=True)
    CCTV_type = models.CharField(verbose_name="Вид системы видеонаблюдения", max_length=50, blank=True, null=True)
    CCTV_complies_safe_city_program = models.BooleanField(
        verbose_name="Соответствует техническим требованиям программы «Безопасный город»", null=True, blank=True)
    indoor_cameras_count = models.IntegerField(verbose_name="Количество камер внутри помещения", blank=True, null=True)
    outdoor_cameras_count = models.IntegerField(verbose_name="Количество наружных камер", blank=True, null=True)
    CCTV_project = models.BooleanField(verbose_name="Наличие проекта на систему видеонаблюдения", null=True, blank=True)
    CCTV_is_workable = models.BooleanField(verbose_name="Техническое состояние системы видеонаблюдения", null=True,
                                           blank=True)
    unworkable_cameras_count = models.IntegerField(verbose_name="Количество неисправных камер", blank=True, null=True)

    class Meta:
        abstract = True
