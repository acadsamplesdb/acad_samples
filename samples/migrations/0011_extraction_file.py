# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0010_auto_20150724_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraction',
            name='file',
            field=models.ManyToManyField(blank=True, to='samples.FileAttachment'),
        ),
    ]
