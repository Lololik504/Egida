from main.models.indoor_areas import *

class IndoorAreas(AdminRoom, Auditorium, Bathroom, Classroom, Corridor, EmergencyExit, FoodBlock,
                  Gym, Laundry, Pantry, Pool):
    class Meta:
        verbose_name = "Внутренние помещения"
