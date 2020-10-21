import datetime

from django.db import models


# Create your models here.

def get_model_fields(model):
    return model._meta.fields


class District(models.Model):
    name = models.CharField(verbose_name="Район", max_length=50)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name


class School(models.Model):
    INN = models.CharField(verbose_name="ИНН", max_length=13, default='', unique=True)
    name = models.CharField(verbose_name="Полное название", max_length=300, default='', unique=True)
    shortname = models.CharField(verbose_name="Краткое название", max_length=100, default='', unique=True)
    phone = models.CharField(verbose_name="Телефон", max_length=100, default='', unique=True)
    address = models.CharField(verbose_name="Адрес", max_length=300, default='', unique=False)
    district = models.ForeignKey(District, verbose_name="Район", on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"

    def update(self, data):
        if "Inn" in data:
            data.pop("Inn")
        for k, v in data.items():
            try:
                setattr(self, k, v)
            except:
                pass
        self.save()

    def __str__(self):
        return self.shortname


class Director(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    patronymic = models.CharField(verbose_name="Отчество", max_length=30)
    school = models.ForeignKey(School, verbose_name="Школа", on_delete=models.DO_NOTHING, default=None)

    class Meta:
        verbose_name = "Директор"
        verbose_name_plural = "Директоры"

    def __str__(self):
        return self.last_name + self.first_name + self.patronymic


class Building(models.Model):
    school = models.ForeignKey(School, verbose_name="Школа", on_delete=models.CASCADE, default=None)
    address = models.CharField(verbose_name="Адрес", max_length=350)

    # TYPE = (
    #     ("FREE_STANDING", "Отдельно стоящее"),
    #     ("BUILD_INTO_APART", "Встроенное в многоквартирный дом"),
    #     ("ATTACHED_TO_APART", "Пристроенное к многоквартирному дому"),
    # )

    class TYPE(models.TextChoices):
        FREE_STANDING = "Отдельно стоящее"
        BUILD_INTO_APART = "Встроенное в многоквартирный дом"
        ATTACHED_TO_APART = "Пристроенное к многоквартирному дому"
    type = models.CharField(verbose_name="Вид здания", max_length=50, choices=TYPE.choices, default=TYPE.FREE_STANDING,
                            blank=True, null=True)

    purpose = models.CharField(verbose_name="Назначение здания", max_length=200, blank=True,
                                null=True)

    YEAR_CHOICES = []
    YEAR_CHOICES_FOR_RESPONSE = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
        YEAR_CHOICES_FOR_RESPONSE.append(r)

    construction_year = models.IntegerField(verbose_name="Год постройки здания", choices=YEAR_CHOICES, default=2000,
                                            blank=True,
                                            null=True)
    building_square = models.IntegerField(verbose_name="Площадь здания", blank=True, null=True)
    land_square = models.IntegerField(verbose_name="Площадь земельного участка", blank=True, null=True)
    number_of_storeys = models.IntegerField(verbose_name="Этажность", blank=True, null=True)
    build_height = models.IntegerField(verbose_name="Высота здания", blank=True, null=True)
    # build_configure = models.ImageField(verbose_name="Конфигурация здания")
    occupancy_proj = models.IntegerField(verbose_name="Наполняемость проектная", blank=True, null=True)
    occupancy_fact = models.IntegerField(verbose_name="Наполняемость фактическая", blank=True, null=True)
    arend_square = models.IntegerField(verbose_name="Площадь зданий/помещений, сдаваемых в аренду", blank=True,
                                       null=True)
    arend_use_type = models.CharField(verbose_name="Вид исспользования", max_length=50, blank=True, null=True)
    unused_square = models.IntegerField(verbose_name="Площадь неиспользуемых зданий/помещений м.кв", blank=True,
                                        null=True)
    repair_need_square = models.IntegerField(verbose_name="Площадь, требующая ремонта", blank=True, null=True)

    class TECHNICAL_CONDITION(models.TextChoices):
        WORKING = "Работоспособное"
        LIMITED_WORKING = "Ограниченно-работоспособное"
        EMERGENCY = "Аварийное"

    technical_condition = models.CharField(verbose_name="Техническое состояние", max_length=50,
                                           choices=TECHNICAL_CONDITION.choices, blank=True, null=True)
    last_repair_year = models.IntegerField(verbose_name="Год последнего капитально ремонта", choices=YEAR_CHOICES,
                                           default=2000, blank=True, null=True)

    def update(self, data):
        if "id" in data:
            data.pop("id")
        for k, v in data.items():
            try:
                setattr(self, k, v)
            except:
                pass
        self.save()

    def get_choices(self):
        res = {
            'TYPE': self.TYPE.values,
            # 'PURPOSE': self.PURPOSE.values,
            'YEAR_CHOICES': self.YEAR_CHOICES_FOR_RESPONSE,
            'TECHNICAL_CONDITION': self.TECHNICAL_CONDITION.values
        }
        return res

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"
