# from django.db import models

from main.models.building_construction import *


# from main.models import *


class BuildingConstruction(BlindArea, Facade, Overlapping, Roof, Window):
    # building = models.OneToOneField(Building, null=True, default=None, on_delete=models.SET_NULL)
    pass

    class Meta:
        verbose_name = "Строительные конструкции"
