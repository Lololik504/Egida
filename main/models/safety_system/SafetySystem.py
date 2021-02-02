from main.models.safety_system import *


class SafetySystem(AfaAndEmc, CCTV):
    class Meta:
        verbose_name = "Система безопасности"
