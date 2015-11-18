# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import gestionies.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dni',
            field=models.CharField(db_index=True, max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='es_usuario',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(upload_to=gestionies.users.models.upload_to, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='id_usuario',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='usuario_rayuela',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
