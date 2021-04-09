import datetime

from django.db import models

from main.MyModelFile import MyModel
from main.models import District
from main.models import School


class Requisites(MyModel):
    school = models.ForeignKey(School, verbose_name="Школа", on_delete=models.CASCADE, default=None)
    district = models.ForeignKey(District, verbose_name="Территориальная принадлежность", on_delete=models.CASCADE,
                                    default=None, null=True)
    official_site = models.CharField(verbose_name="Оффициальный сайт", max_length=100, blank=True, null=True)
    legal_address_street = models.CharField(verbose_name="Юридический адрес (улица)", max_length=100, blank=True,
                                            null=True)
    legal_address_number = models.CharField(verbose_name="Юридический адрес (номер дома)", max_length=100, blank=True,
                                            null=True)
    formation_date = models.DateField(verbose_name="Дата образования юридического лица", max_length=100, null=True,
                                      blank=True,
                                      default=datetime.date.today)

    def __init__(self, *args, **kwargs):
        self.static_fields.append("school")
        models.Model.__init__(self, *args, **kwargs)

    def update(self, data: dict):
        if data.__contains__("district"):
            dist = data["district"]
            data["district"] = District.objects.get(name=dist)
        MyModel.update(self, data)

    class Meta:
        verbose_name = "Реквизиты"
        verbose_name_plural = "Реквизиты"
        app_label = "main"
