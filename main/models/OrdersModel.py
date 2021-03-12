from django.db import models
from main.MyModelFile import MyModel
from Egida.settings import ROSPOTREB_URL, GOSPOZH_URL, ROSTECH_URL, SUDEB_URL, OTHER_ORDERS_URL


def rospotreb_inn_dir_path(instance, filename):
    return ROSPOTREB_URL+ '/inn_{}/{}'.format(instance.school.INN, filename)


def gospozh_inn_dir_path(instance, filename):
    return GOSPOZH_URL + '/inn_{}/{}'.format(instance.school.INN, filename)


def rostech_inn_dir_path(instance, filename):
    return ROSTECH_URL + '/inn_{}/{}'.format(instance.school.INN, filename)


def sudeb_inn_dir_path(instance, filename):
    return SUDEB_URL + '/inn_{}/{}'.format(instance.school.INN, filename)


def other_orders_inn_dir_path(instance, filename):
    return OTHER_ORDERS_URL + '/inn_{}/{}'.format(instance.school.INN, filename)


class Rospotreb(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    date_order = models.DateField(verbose_name='Дата вынесения предписания', default=None, null=True, blank=True)
    type_work = models.TextField(verbose_name='Вид работ', default=None, null=True, blank=True)
    summa = models.FloatField(verbose_name='Сумма', default=None, null=True, blank=True)
    period_execution = models.DateField(verbose_name='Период исполнения', default=None, null=True, blank=True)
    order = models.FileField(verbose_name='Скан предписания', upload_to=rospotreb_inn_dir_path)
    vkluchenie = models.BooleanField(verbose_name='Включение в приказ текущего года по ремонтным работам', default=None,
                                     null=True, blank=True)
    executed = models.BooleanField(verbose_name='Отметка об исполнении', default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Роспотребнадзор'
        verbose_name_plural = 'Роспотребнадзор'
        app_label = 'main'

class Gospozh(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    date_order = models.DateField(verbose_name='Дата вынесения предписания', default=None, null=True, blank=True)
    type_work = models.TextField(verbose_name='Вид работ', default=None, null=True, blank=True)
    summa = models.FloatField(verbose_name='Сумма', default=None, null=True, blank=True)
    period_execution = models.DateField(verbose_name='Период исполнения', default=None, null=True, blank=True)
    order = models.FileField(verbose_name='Скан предписания', upload_to=rospotreb_inn_dir_path)
    vkluchenie = models.BooleanField(verbose_name='Включение в приказ текущего года по ремонтным работам', default=None,
                                     null=True, blank=True)
    executed = models.BooleanField(verbose_name='Отметка об исполнении', default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Госпожнадзор'
        verbose_name_plural = 'Госпожнадзор'
        app_label = 'main'


class Rostech(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    date_order = models.DateField(verbose_name='Дата вынесения предписания', default=None, null=True, blank=True)
    type_work = models.TextField(verbose_name='Вид работ', default=None, null=True, blank=True)
    summa = models.FloatField(verbose_name='Сумма', default=None, null=True, blank=True)
    period_execution = models.DateField(verbose_name='Период исполнения', default=None, null=True, blank=True)
    order = models.FileField(verbose_name='Скан предписания', upload_to=rospotreb_inn_dir_path)
    vkluchenie = models.BooleanField(verbose_name='Включение в приказ текущего года по ремонтным работам', default=None,
                                     null=True, blank=True)
    executed = models.BooleanField(verbose_name='Отметка об исполнении', default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Ростехнадзор'
        verbose_name_plural = 'Ростехнадзор'
        app_label = 'main'


class Sudeb(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    date_order = models.DateField(verbose_name='Дата вынесения предписания', default=None, null=True, blank=True)
    type_work = models.TextField(verbose_name='Вид работ', default=None, null=True, blank=True)
    summa = models.FloatField(verbose_name='Сумма', default=None, null=True, blank=True)
    period_execution = models.DateField(verbose_name='Период исполнения', default=None, null=True, blank=True)
    order = models.FileField(verbose_name='Скан предписания', upload_to=rospotreb_inn_dir_path)
    vkluchenie = models.BooleanField(verbose_name='Включение в приказ текущего года по ремонтным работам', default=None,
                                     null=True, blank=True)
    executed = models.BooleanField(verbose_name='Отметка об исполнении', default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Судебные решения'
        verbose_name_plural = 'Судебные решения'
        app_label = 'main'


class OtherOrders(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    date_order = models.DateField(verbose_name='Дата вынесения предписания', default=None, null=True, blank=True)
    type_work = models.TextField(verbose_name='Вид работ', default=None, null=True, blank=True)
    summa = models.FloatField(verbose_name='Сумма', default=None, null=True, blank=True)
    period_execution = models.DateField(verbose_name='Период исполнения', default=None, null=True, blank=True)
    order = models.FileField(verbose_name='Скан предписания', upload_to=rospotreb_inn_dir_path)
    vkluchenie = models.BooleanField(verbose_name='Включение в приказ текущего года по ремонтным работам', default=None,
                                     null=True, blank=True)
    executed = models.BooleanField(verbose_name='Отметка об исполнении', default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Прочие надзорные органы'
        verbose_name_plural = 'Прочие надзорные органы'
        app_label = 'main'


