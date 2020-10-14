from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import path

from accounts import models as amodels
from .models import *

# Register your models here.

admin.site.register(District)
admin.site.register(School)
admin.site.register(Building)


# admin.site.register(Temperatures)



class YOUR_MODELAdmin(admin.ModelAdmin):
    change_list_template = "admin/monitor_change_list.html"

    @staff_member_required
    def export(self, request):
        print("EXPORT")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("export/", self.export)
        ]
        return my_urls + urls


# admin.site.register(amodels.AdminUser, YOUR_MODELAdmin)
