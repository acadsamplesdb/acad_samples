# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0023_auto_20150818_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='aqissamplegroup',
            name='permit_num',
            field=models.CharField(blank=True, max_length=255, verbose_name='Permit number'),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='group_num',
            field=models.CharField(serialize=False, blank=True, max_length=255, verbose_name='Group number', primary_key=True),
        ),
    ]
