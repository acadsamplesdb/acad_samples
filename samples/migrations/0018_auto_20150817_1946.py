# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0017_auto_20150815_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aqissamplegroup',
            name='samples',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='organism_note',
        ),
        migrations.AddField(
            model_name='sample',
            name='common_name',
            field=models.CharField(verbose_name='Organism common name', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sample',
            name='group_num',
            field=models.ForeignKey(null=True, to='samples.AQISSampleGroup'),
        ),
    ]
