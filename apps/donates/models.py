from django.db import models

from apps.donates.choices import DonatStatusChoice


class Donates(models.Model):
    user_id = models.ForeignKey(to='telegram_users.TelegramUsers', on_delete=models.PROTECT)
    diamond = models.IntegerField()
    status = models.CharField(choices=DonatStatusChoice.choices, default=DonatStatusChoice.NEW.value)
    image = models.ImageField(upload_to='donates/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Donat'
        verbose_name_plural = 'Donates'

    def __str__(self):
        return f"{self.user_id}-{self.diamond}"
