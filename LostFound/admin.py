from django.contrib import admin

from .models import UserRegistration,Lost_Item,Found_Item


admin.site.register(UserRegistration)
admin.site.register(Lost_Item)
admin.site.register(Found_Item)
