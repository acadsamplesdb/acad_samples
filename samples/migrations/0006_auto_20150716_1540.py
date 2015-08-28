# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0005_auto_20150710_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aqissamplegroup',
            options={'verbose_name': 'AQIS sample group'},
        ),
        migrations.AlterField(
            model_name='permit',
            name='active_from',
            field=models.DateField(verbose_name='Active from', blank=True),
        ),
        migrations.AlterField(
            model_name='permit',
            name='conditions',
            field=models.CharField(verbose_name='Conditions', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='permit',
            name='permit_num',
            field=models.CharField(verbose_name='Permit number', max_length=255),
        ),
        migrations.AlterField(
            model_name='permit',
            name='qap',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
