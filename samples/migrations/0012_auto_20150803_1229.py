# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0011_extraction_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractresult',
            name='id',
            field=models.CharField(serialize=False, primary_key=True, max_length=255),
        ),
    ]
