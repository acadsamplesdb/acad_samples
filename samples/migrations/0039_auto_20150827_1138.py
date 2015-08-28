# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0038_sequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='amplification',
            field=models.ForeignKey(null=True, to='samples.Amplification', blank=True),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='enrichment',
            field=models.ForeignKey(null=True, to='samples.Enrichment', blank=True),
        ),
    ]
