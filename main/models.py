import datetime

from django.db import models


# Create your models here.

def get_model_fields(model):
    return model._meta.fields


def get_model_name(model):
    return model._meta.model_name


class MyModel:
    static_fields = ["id"]

    def update(self, data):
        for k, v in data.items():
            if self.static_fields.__contains__(k):
                continue
            try:
                setattr(self, k, v)
            except:
                pass
        self.save()

    # class Meta:
    #     proxy = True


class District(models.Model, MyModel):
    name = models.CharField(verbose_name="Район", max_length=50)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name


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

    def get_director(self):
        if self.director is None:
            self.director = Director.default_director()
        return self.director

    def __str__(self):
        return self.shortname


class Personal(models.Model, MyModel):
    first_name = models.CharField(verbose_name="Имя", max_length=30, default=None, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30, default=None, null=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=30, default=None, null=True)
    phone = models.CharField(verbose_name="Телефон", max_length=30, default=None, null=True)
    email = models.CharField(verbose_name="Email", max_length=50, default=None, null=True)

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"

    def __str__(self):
        ans = ""
        if self.last_name is not None:
            ans += self.last_name
        if self.first_name is not None:
            ans += self.first_name
        if self.patronymic is not None:
            ans += self.patronymic
        if ans == "":
            ans = "-"
        return ans


class Director(Personal):
    school = models.OneToOneField(School, null=True, default=None, on_delete=models.SET_NULL)

    @staticmethod
    def default_director():
        director: Director = Director.objects.create()
        return director

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"


class ZavHoz(Personal):
    school = models.OneToOneField(School, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Завхоз"
        verbose_name_plural = "Завхозы"


class Bookkeeper(Personal):
    school = models.OneToOneField(School, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Бухгалтер"
        verbose_name_plural = "Бухгалтеры"


class Updater(Personal):
    school = models.OneToOneField(School, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Ответственный за заполнение"
        verbose_name_plural = "Ответственные за заполнение"


class Building(models.Model, MyModel):
    school = models.ForeignKey(School, verbose_name="Школа", on_delete=models.CASCADE, default=None)
    street = models.CharField(verbose_name="Улица", max_length=300, blank=True, null=True)
    street_number = models.CharField(verbose_name="Номер дома", max_length=50, blank=True, null=True)

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

    # def update(self, data):
    #     if "id" in data:
    #         data.pop("id")
    #     for k, v in data.items():
    #         try:
    #             setattr(self, k, v)
    #         except:
    #             pass
    #     self.save()

    def get_choices(self):
        res = {
            'TYPE': self.TYPE.values,
            # 'PURPOSE': self.PURPOSE.values,
            'YEAR_CHOICES': self.YEAR_CHOICES_FOR_RESPONSE,
            'TECHNICAL_CONDITION': self.TECHNICAL_CONDITION.values
        }
        return res

    def __str__(self):
        if self.street is None:
            return "-"
        if self.street_number is None:
            return self.street
        return self.street + self.street_number

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"
