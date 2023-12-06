from django.db import models


class WarUser(models.Model):
    user_id = models.ForeignKey(to='telegram_users.TelegramUsers', on_delete=models.PROTECT)
    hero_id = models.ForeignKey(to='heroes.Heroes', on_delete=models.PROTECT)
    gold = models.IntegerField(default=0)
    health = models.IntegerField()
    restore_health = models.IntegerField()
    steal_health = models.IntegerField()
    stealing_health_protection = models.IntegerField()
    magical_attack = models.IntegerField()
    physical_attack = models.IntegerField()
    magical_protection = models.IntegerField()
    physical_protection = models.IntegerField()
    line = models.IntegerField()
    is_attack = models.BooleanField(default=False)
    is_dead = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wars = models.ManyToManyField('wars.Wars', through='wars.WarUsers', related_name='war_user_related')
    equipments = models.ManyToManyField('equipments.Equipments', through='equipments.UserEquipments',
                                        related_name='war_users_related')

    class Meta:
        verbose_name = "War-User"
        verbose_name_plural = "War-Users"

    def __str__(self):
        return f"{self.user_id}"
