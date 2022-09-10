from django.contrib import admin

from .models import Project, Site, Device

class ProjectAdmin(admin.ModelAdmin):
    field = ['name','customer','owner','start_date']
admin.site.register(Project, ProjectAdmin)

class SiteAdmin(admin.ModelAdmin):
    field = ['name', 'address']
admin.site.register(Site, SiteAdmin)

class DeviceAdmin(admin.ModelAdmin):
    field = ['name', 'input_voltage', 'output_voltage']
admin.site.register(Device, DeviceAdmin)
