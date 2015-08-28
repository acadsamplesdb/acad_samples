# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0034_auto_20150825_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c14',
            name='error',
            field=models.PositiveSmallIntegerField(verbose_name='Estimated carbon date error range', blank=True, null=True),
        ),
    ]
