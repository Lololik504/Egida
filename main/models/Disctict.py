


class District(models.Model, MyModel):
    name = models.CharField(verbose_name="Район", max_length=50)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name
