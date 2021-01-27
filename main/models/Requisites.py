


class Requisites(models.Model, MyModel):
    school = models.OneToOneField(School, verbose_name="Школа", on_delete=models.CASCADE, default=None)
    district = models.OneToOneField(District, verbose_name="Территориальная принадлежность", on_delete=models.CASCADE,
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
