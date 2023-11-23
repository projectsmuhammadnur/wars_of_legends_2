import datetime

from django.db import models


def default_user_image_path():
    return 'users/default_user_image_00000001.jpeg'


class TelegramUsers(models.Model):
    chat_id = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    added_by = models.ForeignKey('self', on_delete=models.PROTECT, null=True)
    added_users = models.ManyToManyField('self', through='UserToUsers', through_fields=('adder', 'added'),
                                         symmetrical=False, related_name='adder_my_users')
    cup = models.IntegerField(default=0)
    gold = models.IntegerField(default=2000)
    diamond = models.IntegerField(default=0)
    afk_count = models.IntegerField(default=0)
    punishment_count = models.IntegerField(default=0)
    punishment_created_at = models.DateTimeField(default=datetime.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    heroes = models.ManyToManyField('heroes.Heroes', through='heroes.UserHeroes', related_name='telegram_users_related')
    medals = models.ManyToManyField('medals.Medals', through='medals.UserMedals', related_name='telegram_users_related')

    class Meta:
        verbose_name = "Telegram User"
        verbose_name_plural = "Telegram Users"

    def __str__(self):
        return f"{self.name}"


class UserToUsers(models.Model):
    adder = models.ForeignKey(TelegramUsers, related_name='added_users_relationship', on_delete=models.PROTECT)
    added = models.ForeignKey(TelegramUsers, related_name='has_added_me', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
