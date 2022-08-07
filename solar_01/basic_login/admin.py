from django.contrib import admin

from .models import Roles, User, Project, Site, Device

class UserAdmin(admin.ModelAdmin):
    field = ['name', 'role']
admin.site.register(User, UserAdmin)

class RolesAdmin(admin.ModelAdmin):
    field = ['id', 'name']
admin.site.register(Roles, RolesAdmin)

class ProjectAdmin(admin.ModelAdmin):
    field = ['name']
admin.site.register(Project, ProjectAdmin)

class SiteAdmin(admin.ModelAdmin):
    field = ['name', 'address']
admin.site.register(Site, SiteAdmin)

class DeviceAdmin(admin.ModelAdmin):
    field = ['name', 'input_voltage', 'output_voltage']
admin.site.register(Device, DeviceAdmin)