# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0027_c14_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='c14',
            unique_together=set([('centre', 'centre_num')]),
        ),
    ]
