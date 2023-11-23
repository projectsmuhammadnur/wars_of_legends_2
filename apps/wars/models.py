from django.db import models


class Wars(models.Model):
    day = models.IntegerField(default=1)
    is_started = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField('war_user.WarUser', through='wars.WarUsers',
                                   related_name='wars_related')

    class Meta:
        verbose_name = "War"
        verbose_name_plural = "Wars"

    def __str__(self):
        return f"{self.is_started}"


class WarUsers(models.Model):
    war_id = models.ForeignKey('wars.Wars', on_delete=models.PROTECT)
    user_id = models.ForeignKey('war_user.WarUser', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
