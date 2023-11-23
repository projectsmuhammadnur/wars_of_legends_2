from django.contrib import admin

from apps.heroes.models import Heroes, UserHeroes

admin.site.register(Heroes)
admin.site.register(UserHeroes)
