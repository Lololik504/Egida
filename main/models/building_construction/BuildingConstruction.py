from main.models.building_construction import *


class BuildingConstruction(BlindArea, Facade, Overlapping, Roof, Window, Foundation):
    pass

    class Meta:
        verbose_name = "Строительные конструкции"
