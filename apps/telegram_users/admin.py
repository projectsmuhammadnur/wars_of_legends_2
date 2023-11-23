from django.contrib import admin

from apps.telegram_users.models import TelegramUsers, UserToUsers

admin.site.register(TelegramUsers)
admin.site.register(UserToUsers)
