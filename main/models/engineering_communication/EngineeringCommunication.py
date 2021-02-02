from main.models.engineering_communication import *


class EngineeringCommunication(HeatingSystem, PowerSupply, SurfaceWastewater, WaterSupply):
    class Meta:
        verbose_name = "Инженерные коммуникации"
