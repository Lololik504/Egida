from django.contrib import admin

from .models.BuildingModel import Building
from .models.DistrictModel import District
from .models.PersonalModel import Director, ZavHoz, Bookkeeper, Updater
from .models.RequisitesModel import Requisites
from .models.SchoolModel import School
from .models.TemperatureModel import Temperature
from .models.building_construction import BuildingConstruction
from .models.engineering_communication import EngineeringCommunication

admin.site.register(District)

admin.site.register(School)
admin.site.register(Building)

# admin.site.register(Personal)
admin.site.register(Director)
admin.site.register(ZavHoz)
admin.site.register(Bookkeeper)
admin.site.register(Updater)
admin.site.register(Temperature)
admin.site.register(Requisites)
admin.site.register(BuildingConstruction)
admin.site.register(EngineeringCommunication)





class AuthorAdmin(admin.ModelAdmin):
    change_list_template = 'admin/main/School/change_list.html'
