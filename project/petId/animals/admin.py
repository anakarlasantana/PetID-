from django.contrib import admin
from .models.rg import RGRequest, AnimalType, Template


admin.site.register(RGRequest)
admin.site.register(AnimalType)
admin.site.register(Template)

