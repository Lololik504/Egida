from django.contrib import admin

from .models import *

admin.site.register(District)
admin.site.register(School)
admin.site.register(Building)


class AuthorAdmin(admin.ModelAdmin):
    change_list_template = 'admin/main/School/change_list.html'
