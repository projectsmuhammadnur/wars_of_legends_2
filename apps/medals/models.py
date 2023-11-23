from django.db import models

from apps.telegram_users.models import TelegramUsers


class Medals(models.Model):
    name = models.CharField(max_length=255, unique=True)
    gold = models.IntegerField()
    description = models.TextField()
    users = models.ManyToManyField('telegram_users.TelegramUsers', through='medals.UserMedals',
                                   related_name='medals_related')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Medal"
        verbose_name_plural = "Medals"

    def __str__(self):
        return f"{self.name}"


class UserMedals(models.Model):
    user = models.ForeignKey('telegram_users.TelegramUsers', on_delete=models.PROTECT)
    medal = models.ForeignKey('medals.Medals', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
