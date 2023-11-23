from django.db import models


class Equipments(models.Model):
    image = models.ImageField(upload_to='equipments/')
    name = models.CharField(max_length=255, unique=True)
    salary = models.IntegerField()
    health = models.IntegerField()
    restore_health = models.IntegerField()
    steal_health = models.IntegerField()
    stealing_health_protection = models.IntegerField()
    magical_attack = models.IntegerField()
    physical_attack = models.IntegerField()
    magical_protection = models.IntegerField()
    physical_protection = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField('war_user.WarUser', through='equipments.UserEquipments',
                                   related_name='equipments_related')

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'


class UserEquipments(models.Model):
    user = models.ForeignKey('war_user.WarUser', on_delete=models.PROTECT)
    equipment = models.ForeignKey('equipments.Equipments', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
