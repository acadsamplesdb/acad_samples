# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0028_auto_20150821_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c14',
            name='burnweight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='burnyield',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='cnratio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='del13',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='del15',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='nyield',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='pcbyield',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='pyield',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='slug',
            field=models.SlugField(unique=True, max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='use_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='c14',
            unique_together=set([]),
        ),
    ]
