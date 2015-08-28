# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('samples', '0002_auto_20150706_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='samples',
            new_name='sample',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='users',
            new_name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='group',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
