from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    field = ['username', 'email', 'password1','password2']
admin.site.register(User, UserAdmin)

