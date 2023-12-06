from django.db import models

from apps.heroes.choices import HeroRoleChoice


class Heroes(models.Model):
    image = models.ImageField(upload_to='heroes/')
    name = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=10, choices=HeroRoleChoice.choices)
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
    users = models.ManyToManyField('telegram_users.TelegramUsers', through='heroes.UserHeroes',
                                   related_name='heroes_related')

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Heroes"

    def __str__(self):
        return f"{self.name}"


class UserHeroes(models.Model):
    user = models.ForeignKey('telegram_users.TelegramUsers', on_delete=models.PROTECT)
    hero = models.ForeignKey('heroes.Heroes', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
