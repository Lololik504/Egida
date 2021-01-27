


class School(models.Model, MyModel):
    static_fields = MyModel.static_fields + ["INN"]

    district = models.ForeignKey(District, verbose_name="Район", on_delete=models.CASCADE, default=None)

    INN = models.CharField(verbose_name="ИНН", max_length=13, default='', unique=True)
    name = models.CharField(verbose_name="Полное название", max_length=300, default='')
    shortname = models.CharField(verbose_name="Краткое название", max_length=100, default='', unique=True)
    phone = models.CharField(verbose_name="Телефон", max_length=100, default='')
    address = models.CharField(verbose_name="Адрес", max_length=300, default='')
    edu_type = models.CharField(verbose_name="Вид образования", max_length=20, default='')
    form_type = models.CharField(verbose_name="Вид организационно-правовой формы", max_length=20, default='')

    class Meta:
        verbose_name = "Основные сведения"
        verbose_name_plural = "Школы"

    @classmethod
    def create(self, **data: dict):
        district = District.objects.get(name=data['district'])
        data['district'] = district
        return School.objects.create(**data)

    def __str__(self):
        return self.shortname
