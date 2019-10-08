from django.contrib import admin

from .models import PhoneModel, Phone, Part, Storage

admin.site.register(PhoneModel)
admin.site.register(Phone)
admin.site.register(Part)
admin.site.register(Storage)
