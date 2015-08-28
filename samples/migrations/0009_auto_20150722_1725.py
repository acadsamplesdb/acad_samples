# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0008_auto_20150722_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extractresult',
            name='sample',
        ),
        migrations.AddField(
            model_name='extractresult',
            name='sample',
            field=models.ForeignKey(default=1, to='samples.Sample'),
            preserve_default=False,
        ),
    ]
