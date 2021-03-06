from django.contrib import admin
from rango.models import UserProfile
from rango.models import Bar, Tapa

# Add in this class to customized the Admin Interface
class BarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Bar, BarAdmin)
admin.site.register(Tapa)
admin.site.register(UserProfile)

# Register your models here.
