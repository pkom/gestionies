# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(unique=True, max_length=9, db_index=True)),
                ('delays_for_warning', models.PositiveSmallIntegerField(default=2)),
                ('delays_quarterly', models.BooleanField(default=True)),
                ('first_quarter_start', models.DateField()),
                ('first_quarter_end', models.DateField()),
                ('second_quarter_start', models.DateField()),
                ('second_quarter_end', models.DateField()),
                ('third_quarter_start', models.DateField()),
                ('third_quarter_end', models.DateField()),
                ('weight_1', models.DecimalField(default=100, max_digits=5, decimal_places=2)),
                ('weight_2', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('weight_3', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('weight_4', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('weight_5', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('weight_6', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='course', editable=False)),
            ],
            options={
                'ordering': ['course'],
            },
        ),
    ]
