# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.CharField(help_text='Academic course', unique=True, max_length=9, verbose_name='Course', db_index=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='delays_for_warning',
            field=models.PositiveSmallIntegerField(default=2, help_text='Number of delays for warning', verbose_name='Delays for warning'),
        ),
        migrations.AlterField(
            model_name='course',
            name='delays_quarterly',
            field=models.BooleanField(default=True, help_text='Reset delays by quarter', verbose_name='Delays by quarter'),
        ),
        migrations.AlterField(
            model_name='course',
            name='first_quarter_end',
            field=models.DateField(help_text='First quarter end date', verbose_name='First quarter end date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='first_quarter_start',
            field=models.DateField(help_text='First quarter start date', verbose_name='First quarter start date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='second_quarter_end',
            field=models.DateField(help_text='Second quarter end date', verbose_name='Second quarter end date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='second_quarter_start',
            field=models.DateField(help_text='Second quarter start date', verbose_name='Second quarter start date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='third_quarter_end',
            field=models.DateField(help_text='Third quarter end date', verbose_name='Third quarter end date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='third_quarter_start',
            field=models.DateField(help_text='Third quarter start date', verbose_name='Third quarter start date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='weight_1',
            field=models.DecimalField(default=100, help_text='Weight assigned to first criterion evaluation', verbose_name='Weight assigned to first criterion evaluation', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='weight_2',
            field=models.DecimalField(default=0, help_text='Weight assigned to second criterion evaluation', verbose_name='Weight assigned to second criterion evaluation', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='weight_3',
            field=models.DecimalField(default=0, help_text='Weight assigned to third criterion evaluation', verbose_name='Weight assigned to third criterion evaluation', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='weight_4',
            field=models.DecimalField(default=0, help_text='Weight assigned to fourth criterion evaluation', verbose_name='Weight assigned to fourth criterion evaluation', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='weight_5',
            field=models.DecimalField(default=0, help_text='Weight assigned to fifth criterion evaluation', verbose_name='Weight assigned to fifth criterion evaluation', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='weight_6',
            field=models.DecimalField(default=0, help_text='Weight assigned to sixth criterion evaluation', verbose_name='Weight assigned to sixth criterion evaluation', max_digits=5, decimal_places=2),
        ),
    ]
