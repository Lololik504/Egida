from django.db import models
from main.MyModelFile import MyModel
from Egida.settings import MANDATE_URL


def inn_dir_path(instance, filename):
    return MANDATE_URL + '/inn_{}/{}'.format(instance.school.INN, filename)


class MandateCouncil(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    deputy = models.TextField(verbose_name='ФИО Депутата', blank=True, null=True)
    number = models.TextField(verbose_name='Номер наказа', blank=True, null=True)
    region = models.TextField(verbose_name='Округ', blank=True, null=True)
    local_budget = models.FloatField(verbose_name='Местный бюджет', blank=True, null=True)
    regional_budget = models.FloatField(verbose_name='Областной бюджет', blank=True, null=True)
    federal_budget = models.FloatField(verbose_name='Федеральный бюджет', blank=True, null=True)
    appointment = models.TextField(verbose_name='Назначение наказа', blank=True, null=True)
    content = models.TextField(verbose_name='Содержание наказа', blank=True, null=True)
    event = models.TextField(verbose_name='Мероприятия по реализации', blank=True, null=True)
    period_execution = models.TextField(verbose_name='Срок исполнения наказа', blank=True, null=True)
    current_year = models.BooleanField(verbose_name='Включение в приказ текущего года по ремонтным работам', blank=True,
                                       null=True)
    executor = models.TextField(verbose_name='Ответственный исполнитель', blank=True, null=True)
    agreed = models.BooleanField(verbose_name='Согласован', blank=True, null=True)
    file = models.FileField(verbose_name='Файл', upload_to=inn_dir_path, blank=True, null=True)
    fully_executed = models.BooleanField(verbose_name='Исполнено полностью', blank=True, null=True)
    particially_executed = models.BooleanField(verbose_name='Исполнено частично по плану текущего года', blank=True,
                                               null=True)
    actual_cost = models.FloatField(verbose_name='Фактическая стоимость', blank=True, null=True)

    class Meta:
        verbose_name = "Наказ избирателей Совета депутатов г. Новосибирска"
        verbose_name_plural = "Наказы избирателей Совета депутатов г. Новосибирска"


class MandateAssembly(MyModel):
    school = models.ForeignKey(to="main.School", verbose_name="Школа", on_delete=models.CASCADE, default=None)
    deputy = models.TextField(verbose_name='ФИО Депутата', blank=True, null=True)
    number = models.TextField(verbose_name='Номер наказа', blank=True, null=True)
    region = models.TextField(verbose_name='Округ', blank=True, null=True)
    local_budget = models.FloatField(verbose_name='Местный бюджет', blank=True, null=True)
    regional_budget = models.FloatField(verbose_name='Областной бюджет', blank=True, null=True)
    federal_budget = models.FloatField(verbose_name='Федеральный бюджет', blank=True, null=True)
    appointment = models.TextField(verbose_name='Назначение наказа', blank=True, null=True)
    content = models.TextField(verbose_name='Содержание наказа', blank=True, null=True)
    event = models.TextField(verbose_name='Мероприятия по реализации', blank=True, null=True)
    period_execution = models.TextField(verbose_name='Срок исполнения наказа', blank=True, null=True)
    current_year = models.BooleanField(verbose_name='Включение в приказ текущего года по ремонтным работам', blank=True,
                                       null=True)
    executor = models.TextField(verbose_name='Ответственный исполнитель', blank=True, null=True)
    agreed = models.BooleanField(verbose_name='Согласован', blank=True, null=True)
    file = models.FileField(verbose_name='Файл', upload_to=inn_dir_path, blank=True, null=True)
    fully_executed = models.BooleanField(verbose_name='Исполнено полностью', blank=True, null=True)
    particially_executed = models.BooleanField(verbose_name='Исполнено частично по плану текущего года', blank=True,
                                               null=True)
    actual_cost = models.FloatField(verbose_name='Фактическая стоимость', blank=True, null=True)

    class Meta:
        verbose_name = "Наказ избирателей Законодательного собрания НСО"
        verbose_name_plural = "Наказы избирателей Законодательного собрания НСО"
