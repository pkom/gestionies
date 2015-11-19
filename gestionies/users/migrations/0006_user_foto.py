# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import gestionies.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(help_text='User photo', upload_to=gestionies.users.models.upload_to, verbose_name='User photo', blank=True),
        ),
    ]
