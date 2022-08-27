from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Properties, Project, Site, Device

class UserRole(admin.StackedInline):
    model = Properties
    can_delete = False
    verbose_name_plural = 'roles'

class UserAdmin(BaseUserAdmin):
    inlines = (UserRole,)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ProjectAdmin(admin.ModelAdmin):
    field = ['name']
admin.site.register(Project, ProjectAdmin)

class SiteAdmin(admin.ModelAdmin):
    field = ['name', 'address']
admin.site.register(Site, SiteAdmin)

class DeviceAdmin(admin.ModelAdmin):
    field = ['name', 'input_voltage', 'output_voltage']
admin.site.register(Device, DeviceAdmin)