
from django.contrib import admin
from .models import PhoneModel, Phone, Part

admin.site.register(PhoneModel)
admin.site.register(Phone)
admin.site.register(Part)