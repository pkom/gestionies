# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import gestionies.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151118_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Card ID Number', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='es_usuario',
            field=models.BooleanField(default=False, verbose_name='Is Rayuela User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_usuario',
            field=models.CharField(max_length=20, verbose_name='Rayuela User ID', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='usuario_rayuela',
            field=models.CharField(max_length=50, verbose_name='Rayuela User', blank=True),
        ),
    ]
