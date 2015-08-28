# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0037_enrichment_enrichmentresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('path', models.TextField(verbose_name='Path to sequencing files')),
                ('amplification', models.ForeignKey(to='samples.Amplification')),
                ('enrichment', models.ForeignKey(to='samples.Enrichment')),
            ],
        ),
    ]
