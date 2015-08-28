# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0007_auto_20150716_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='datum',
            field=models.CharField(verbose_name='Map or GPS datum from which lat/lon taken', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sample',
            name='extracted_by_date',
            field=models.CharField(verbose_name='Extracted by/date', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sample',
            name='mismatch_reason',
            field=models.CharField(verbose_name='Mismatch reason', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sample',
            name='organism_notes',
            field=models.CharField(verbose_name='Organism note', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sample',
            name='other_notes',
            field=models.CharField(verbose_name='Other notes', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sample',
            name='quality',
            field=models.CharField(verbose_name='Quality', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_repat',
            field=models.CharField(verbose_name='Sample repatriated', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='sample',
            name='carbondate_error',
            field=models.PositiveSmallIntegerField(verbose_name='Estimated carbon date error range', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='lat',
            field=models.CharField(verbose_name='Latitude', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='sample',
            name='lon',
            field=models.CharField(verbose_name='Longitude', blank=True, max_length=255),
        ),
    ]
