# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0018_auto_20150817_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='group_num',
        ),
        migrations.AddField(
            model_name='sample',
            name='group',
            field=models.ForeignKey(to='samples.AQISSampleGroup', null=True, blank=True),
        ),
    ]
