# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0030_auto_20150825_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='c14',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, default='1', primary_key=True, auto_created=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='c14',
            name='slug',
            field=models.SlugField(null=True, max_length=255, blank=True),
        ),
    ]
