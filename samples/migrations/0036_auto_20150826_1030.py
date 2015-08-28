# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0035_auto_20150826_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c14',
            name='burnweight',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='burnyield',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='cnratio',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='del13',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='del15',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='mg_c',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='nyield',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='pcbyield',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='percent_c',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='pyield',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='use_weight',
            field=models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True),
        ),
    ]
