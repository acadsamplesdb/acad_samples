# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0026_auto_20150821_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='c14',
            name='slug',
            field=models.SlugField(null=True, max_length=255, blank=True),
        ),
    ]
