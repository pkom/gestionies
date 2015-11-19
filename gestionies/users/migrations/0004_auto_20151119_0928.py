# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import gestionies.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151119_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.CharField(help_text='Card ID Number', max_length=20, verbose_name='Card ID Number', db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='es_usuario',
            field=models.BooleanField(default=False, help_text='Is Rayuela User', verbose_name='Is Rayuela User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_usuario',
            field=models.CharField(help_text='Rayuela User ID', max_length=20, verbose_name='Rayuela User ID', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(help_text='Name of User', max_length=255, verbose_name='Name of User', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='usuario_rayuela',
            field=models.CharField(help_text='Rayuela User', max_length=50, verbose_name='Rayuela User', blank=True),
        ),
    ]
