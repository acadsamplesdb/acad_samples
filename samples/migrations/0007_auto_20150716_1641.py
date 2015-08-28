# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0006_auto_20150716_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='permit',
            name='file',
            field=models.ManyToManyField(blank=True, to='samples.FileAttachment'),
        ),
        migrations.AlterField(
            model_name='permit',
            name='conditions',
            field=models.TextField(blank=True, verbose_name='Conditions', max_length=255),
        ),
    ]
