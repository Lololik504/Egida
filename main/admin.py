from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(District)
admin.site.register(School)

# admin.site.register(Entity)
# admin.site.register(RepairWorks)
# admin.site.register(Mandates)
# admin.site.register(DeputiesOrders)
# admin.site.register(Documentation)
#
# admin.site.register(EngineeringStructures)
# admin.site.register(IndoorSpaces)
# admin.site.register(SafetySystem)
# admin.site.register(Landscaping)
# admin.site.register(SportsFacilietes)
admin.site.register(Temperatures)
