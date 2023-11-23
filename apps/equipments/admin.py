from django.contrib import admin

from apps.equipments.models import Equipments, UserEquipments

admin.site.register(Equipments)
admin.site.register(UserEquipments)
