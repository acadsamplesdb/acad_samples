# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0031_auto_20150825_1451'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='c14',
            unique_together=set([('centre', 'centre_num')]),
        ),
    ]
