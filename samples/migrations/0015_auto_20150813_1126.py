# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0014_auto_20150811_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c14',
            name='centre_id',
        ),
        migrations.RemoveField(
            model_name='c14',
            name='excess',
        ),
        migrations.RemoveField(
            model_name='c14',
            name='pos',
        ),
        migrations.RemoveField(
            model_name='c14',
            name='wheel',
        ),
        migrations.AddField(
            model_name='c14',
            name='centre',
            field=models.CharField(max_length=255, default='fred', verbose_name='Centre that did carbon dating'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c14',
            name='centre_num',
            field=models.CharField(max_length=255, default=1234, verbose_name='Centre reference number'),
            preserve_default=False,
        ),
    ]
