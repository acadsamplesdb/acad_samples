# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0021_auto_20150818_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amplification',
            name='method',
            field=models.TextField(verbose_name='Method', help_text='e.g. library prep or PCR'),
        ),
        migrations.AlterField(
            model_name='amplification',
            name='prepared_by',
            field=models.CharField(max_length=255, verbose_name='Prepared by'),
        ),
    ]
