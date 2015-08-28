# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0013_auto_20150807_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='extractresult',
            name='dna_yield',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='extractresult',
            name='quant_method',
            field=models.CharField(verbose_name='Quantification method', max_length=255, blank=True, choices=[('tapestation', 'TapeStation'), ('nanodrop', 'NanoDrop'), ('qpcr', 'qPCR')]),
        ),
    ]
