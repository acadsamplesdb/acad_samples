# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0015_auto_20150813_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='c14',
            old_name='carbondate',
            new_name='date',
        ),
    ]
