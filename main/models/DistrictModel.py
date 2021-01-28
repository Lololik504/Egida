from django.db import models

from main.MyModelFile import MyModel


class District(MyModel):
    name = models.CharField(verbose_name="Район", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"
        app_label = "main"
