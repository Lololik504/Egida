from django.db import models

from main.MyModelFile import MyModel


class AccessibilityPassport(MyModel):
    accessibility_passport_agreed = models.BooleanField(verbose_name="Паспорт доступности согласован", blank=True,
                                                        null=True)
    accessibility_passport_published_on_site = models.BooleanField(
        verbose_name="Паспорт доступности Опубликован на сайте образовательного учреждения", blank=True, null=True)

    class Meta:
        abstract = True
