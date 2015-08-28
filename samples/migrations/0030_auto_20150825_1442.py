# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0029_auto_20150825_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c14',
            name='id',
        ),
        migrations.AlterField(
            model_name='c14',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False, blank=True, max_length=255),
        ),
    ]
