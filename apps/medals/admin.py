from django.contrib import admin

from apps.medals.models import Medals, UserMedals

admin.site.register(Medals)
admin.site.register(UserMedals)
