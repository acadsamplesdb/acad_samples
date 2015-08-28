# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0024_auto_20150819_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='aqissamplegroup',
            name='group_num_int',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
