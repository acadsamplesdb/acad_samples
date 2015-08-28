# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0009_auto_20150722_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='organism_notes',
            new_name='organism_note',
        ),
        migrations.AddField(
            model_name='sample',
            name='file',
            field=models.ManyToManyField(to='samples.FileAttachment', blank=True),
        ),
    ]
