# Generated by Django 4.2.7 on 2023-11-23 09:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('heroes', '0001_initial'),
        ('medals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('cup', models.IntegerField(default=0)),
                ('gold', models.IntegerField(default=2000)),
                ('diamond', models.IntegerField(default=0)),
                ('afk_count', models.IntegerField(default=0)),
                ('punishment_count', models.IntegerField(default=0)),
                ('punishment_created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='telegram_users.telegramusers')),
            ],
            options={
                'verbose_name': 'Telegram User',
                'verbose_name_plural': 'Telegram Users',
            },
        ),
        migrations.CreateModel(
            name='UserToUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='has_added_me', to='telegram_users.telegramusers')),
                ('adder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='added_users_relationship', to='telegram_users.telegramusers')),
            ],
        ),
        migrations.AddField(
            model_name='telegramusers',
            name='added_users',
            field=models.ManyToManyField(related_name='adder_my_users', through='telegram_users.UserToUsers', to='telegram_users.telegramusers'),
        ),
        migrations.AddField(
            model_name='telegramusers',
            name='heroes',
            field=models.ManyToManyField(related_name='telegram_users_related', through='heroes.UserHeroes', to='heroes.heroes'),
        ),
        migrations.AddField(
            model_name='telegramusers',
            name='medals',
            field=models.ManyToManyField(related_name='telegram_users_related', through='medals.UserMedals', to='medals.medals'),
        ),
    ]
