# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0022_auto_20150818_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='group_num',
            field=models.CharField(serialize=False, verbose_name='Group number', primary_key=True, max_length=255),
        ),
    ]
