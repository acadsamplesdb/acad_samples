# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0032_auto_20150825_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileattachment',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='File name'),
        ),
        migrations.AlterField(
            model_name='fileattachment',
            name='size',
            field=models.PositiveIntegerField(blank=True, verbose_name='File size'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='group',
            field=models.ForeignKey(to='samples.AQISSampleGroup', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True),
        ),
    ]
