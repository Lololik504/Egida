from main.models.accessible_environment import *


class AccessibleEnvironment(AccessibilityPassport, Bathroom, BuildingEntrance, FloorsMovement, StreetTerritory):
    class Meta:
        verbose_name = "Доступная среда"
