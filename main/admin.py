from django.contrib import admin

from .models.BuildingModel import Building
from .models.DistrictModel import District
from .models.PersonalModel import Director, ZavHoz, Bookkeeper, Updater, PlumberLocksmith, Electrician

from .models.RequisitesModel import Requisites
from .models.SchoolModel import School
from .models.TemperatureModel import Temperature

from .models.building_construction import BuildingConstruction
from .models.engineering_communication import EngineeringCommunication
from .models.safety_system import SafetySystem
from .models.territory_improvement import TerritoryImprovement
from .models.accessible_environment import AccessibleEnvironment
from .models.indoor_areas import IndoorAreas
from .models.sports_facilities import SportsFacilities
from .models.DocumentsModel import Document
from .models.OrdersModel import Rospotreb, Gospozh, Rostech, Sudeb, OtherOrders


admin.site.register(District)

admin.site.register(School)
admin.site.register(Building)

admin.site.register(Director)
admin.site.register(ZavHoz)
admin.site.register(Bookkeeper)
admin.site.register(Updater)
admin.site.register(PlumberLocksmith)
admin.site.register(Electrician)
admin.site.register(Temperature)
admin.site.register(Requisites)

admin.site.register(BuildingConstruction)
admin.site.register(EngineeringCommunication)
admin.site.register(SafetySystem)
admin.site.register(TerritoryImprovement)
admin.site.register(AccessibleEnvironment)
admin.site.register(IndoorAreas)
admin.site.register(SportsFacilities)
admin.site.register(Document)
admin.site.register(Rospotreb)
admin.site.register(Gospozh)
admin.site.register(Rostech)
admin.site.register(Sudeb)
admin.site.register(OtherOrders)
