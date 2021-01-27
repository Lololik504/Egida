from django.contrib import admin

from .models import *

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



class AuthorAdmin(admin.ModelAdmin):
    change_list_template = 'admin/main/School/change_list.html'
