

class Temperature(models.Model, MyModel):
    air_temperature = models.FloatField(null=True, verbose_name="Температура воздуха")
    coolant_forward_temperature = models.FloatField(null=True, verbose_name="Температура подающего трубопровода")
    coolant_backward_temperature = models.FloatField(null=True, verbose_name="Температура обратного трубопровода")
    forward_pressure = models.FloatField(null=True, verbose_name="Давление на подающем трубопроводе")
    backward_pressure = models.FloatField(null=True, verbose_name="Давление на обратном трубопроводе")
    building = models.ForeignKey(Building, null=False, verbose_name="Здание", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Дата", null=False, default=datetime.date.today)

    def __str__(self):
        return "Здание {0} температура воздуха: {1}".format(self.building, self.air_temperature)

    def save(self, *args, **kwargs):
        if parse_date(self.date) > datetime.date.today():
            raise ValidationError('Некорректная дата')
        super(Temperature, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Температурный режим"
        verbose_name_plural = "Температуры"
