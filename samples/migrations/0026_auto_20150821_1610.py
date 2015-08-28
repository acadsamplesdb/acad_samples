# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0025_aqissamplegroup_group_num_int'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aqissamplegroup',
            options={'verbose_name': 'AQIS sample group', 'ordering': ['-group_num_int', '-group_num']},
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='group_num_int',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
