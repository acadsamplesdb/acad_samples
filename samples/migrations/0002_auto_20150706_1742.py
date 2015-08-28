# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='carbondate_error',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Estimated carbon date error range'),
        ),
        migrations.AddField(
            model_name='sample',
            name='carbondate_id',
            field=models.CharField(max_length=255, blank=True, verbose_name='Centre + id reference for carbon dating'),
        ),
        migrations.AddField(
            model_name='sample',
            name='carbondate_years',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Estimated age in radiocarbon years'),
        ),
    ]
