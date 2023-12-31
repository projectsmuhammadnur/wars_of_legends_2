# Generated by Django 4.2.7 on 2023-11-23 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('telegram_users', '0001_initial'),
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userheroes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='telegram_users.telegramusers'),
        ),
        migrations.AddField(
            model_name='heroes',
            name='users',
            field=models.ManyToManyField(related_name='heroes_related', through='heroes.UserHeroes', to='telegram_users.telegramusers'),
        ),
    ]
