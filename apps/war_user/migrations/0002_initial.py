# Generated by Django 4.2.7 on 2023-11-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('war_user', '0001_initial'),
        ('wars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waruser',
            name='wars',
            field=models.ManyToManyField(related_name='war_user_related', through='wars.WarUsers', to='wars.wars'),
        ),
    ]
