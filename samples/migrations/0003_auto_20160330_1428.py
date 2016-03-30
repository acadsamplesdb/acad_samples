# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_auto_20151208_0322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fileattachment',
            options={'ordering': ['name', 'size']},
        ),
        migrations.AlterModelOptions(
            name='sample',
            options={'ordering': ['acad_num']},
        ),
        migrations.AlterField(
            model_name='amplificationresult',
            name='dna_yield',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5, blank=True),
        ),
        migrations.AlterField(
            model_name='enrichmentresult',
            name='dna_yield',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5, blank=True),
        ),
        migrations.AlterField(
            model_name='extractresult',
            name='dna_yield',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5, blank=True),
        ),
        migrations.AlterField(
            model_name='permit',
            name='active_from',
            field=models.DateField(verbose_name='Active from', null=True, blank=True),
        ),
    ]
