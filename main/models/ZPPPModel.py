from main.MyModelFile import MyModel
from django.db import models


# Заглубленные помещения подземеного пространства

class ZPPP(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    type_ownership = models.TextField(verbose_name='Форма собственности', null=True, blank=True)
    zppp_group = models.IntegerField(verbose_name='Группа ЗППП', null=True, blank=True)
    zppp_height = models.FloatField(verbose_name='Высота ЗППП', null=True, blank=True)
    zppp_square = models.FloatField(verbose_name='Общая площадь ЗППП', null=True, blank=True)
    zppp_material = models.TextField(verbose_name='Материал наружных стен ЗППП', null=True, blank=True)
    zppp_heating = models.BooleanField(verbose_name='Наличие отопления ЗППП', null=True, blank=True)
    zppp_water = models.BooleanField(verbose_name='Наличие водоразборных кранов холодного и горячего водоснабжения в ЗППП', null=True, blank=True)
    zppp_sewerage = models.BooleanField(verbose_name='Наличие канализации в ЗППП', null=True, blank=True)
    zppp_light = models.BooleanField(verbose_name='Наличие освещения', null=True, blank=True)
    zppp_ventilation = models.BooleanField(verbose_name='Наличие принудительной вентиляции в ЗППП', null=True, blank=True)
    zppp_additional = models.TextField(verbose_name='Дополнительные сведения', null=True, blank=True)

    class Meta:
        verbose_name = 'Заглубленные помещения подземеного пространства'
        verbose_name_plural = 'Заглубленные помещения подземеного пространства'
