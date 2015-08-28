# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0016_auto_20150813_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileattachment',
            name='name',
            field=models.CharField(verbose_name='File name', max_length=255, default='fred'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileattachment',
            name='size',
            field=models.PositiveIntegerField(verbose_name='File size', default=66),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extractresult',
            name='final_vol',
            field=models.CharField(verbose_name='Final DNA volume', help_text='(in ul)', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='extractresult',
            name='starting',
            field=models.CharField(verbose_name='Starting material', max_length=255, blank=True),
        ),
    ]
