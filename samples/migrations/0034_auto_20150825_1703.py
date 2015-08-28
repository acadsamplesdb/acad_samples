# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0033_auto_20150825_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c14',
            name='date',
            field=models.CharField(verbose_name='Estimated age in radiocarbon years', max_length=255),
        ),
    ]
