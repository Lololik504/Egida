from django.db import models

from main.MyModelFile import MyModel


class AfaAndEmc(MyModel):  # Automatic Fire Alarm and Evacuation Management System
    APS_installation_year = models.IntegerField(verbose_name="Год установки АПС", blank=True, null=True)
    APS_and_SOUE_service_organization_name = models.CharField(
        verbose_name="Наименование обслуживающей организации (АПС и СОУЭ)", max_length=50,
        null=True, blank=True)

    price_for_APS_and_SOUE_per_year = models.FloatField(
        verbose_name="Сумма на обслуживание АПС и СОУЭ в год (тыс. руб.)", blank=True, null=True)
    ##############################################################################
    APS_modernization_year = models.IntegerField(verbose_name="Год модернизации АПС", blank=True, null=True)
    APS_project = models.BooleanField(verbose_name="Наличие проекта на АПС", null=True, blank=True)
    APS_compliance_with_the_project = models.BooleanField(
        verbose_name="Соответствие проектной документации с установленной АПС", null=True, blank=True)
    APS_type = models.CharField(verbose_name="Вид АПС", max_length=50, null=True, blank=True)
    ###########################################
    SOUE_installation_year = models.IntegerField(verbose_name="Год установки СОУЭ", blank=True, null=True)
    SOUE_type = models.IntegerField(verbose_name="Тип СОУЭ", blank=True, null=True)
    SOUE_project = models.BooleanField(verbose_name="Наличие проекта на СОУЭ", null=True, blank=True)
    SOUE_compliance_with_the_project = models.BooleanField(
        verbose_name="Соответствие проектной документации с установленной СОУЭ", null=True, blank=True)
    #############################################
    APS_and_SOUE_disadvantages = models.TextField(
        verbose_name="Недостатки, прописанные в акте обслуживающей АПС и СОУЭ организации", null=True, blank=True)

    automatic_smoke_exhaust = models.BooleanField(verbose_name="Наличие системы автоматического дымоудаления",
                                                  null=True, blank=True)

    ASE_service_organization_name = models.CharField(
        verbose_name="Наименование обслуживающей организации (Система автоматического дымоудаления)", max_length=50,
        null=True, blank=True)
    price_for_ASE_per_year = models.FloatField(
        verbose_name="Сумма на обслуживание системы автоматического дымоудаления в год (тыс. руб.)", blank=True,
        null=True)

    class Meta:
        abstract = True
