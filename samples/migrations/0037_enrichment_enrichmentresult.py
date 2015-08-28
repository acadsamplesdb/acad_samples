# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0036_auto_20150826_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrichment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('prepared_by', models.CharField(max_length=255, verbose_name='Prepared by')),
                ('notes', models.TextField(blank=True)),
                ('file', models.ManyToManyField(to='samples.FileAttachment', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnrichmentResult',
            fields=[
                ('id', models.CharField(serialize=False, max_length=255, blank=True, primary_key=True)),
                ('enrich_type', models.CharField(help_text='e.g. Mito, 10k', max_length=255, verbose_name='Enrichment type', blank=True)),
                ('bait_detail', models.CharField(help_text='MyBait batch number', max_length=255, verbose_name='Bait detail', blank=True)),
                ('dna_yield', models.PositiveIntegerField(null=True, blank=True)),
                ('quant_method', models.CharField(max_length=255, verbose_name='Quantification method', blank=True)),
                ('ampresult', models.ForeignKey(to='samples.AmplificationResult')),
                ('enrichment', models.ForeignKey(to='samples.Enrichment')),
            ],
        ),
    ]
