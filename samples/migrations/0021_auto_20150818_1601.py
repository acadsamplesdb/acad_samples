# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0020_auto_20150818_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amplification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('prepared_by', models.CharField(blank=True, verbose_name='Prepared by', max_length=255)),
                ('method', models.TextField(blank=True, verbose_name='Method', help_text='e.g. library prep or PCR')),
                ('amp_type', models.CharField(blank=True, verbose_name='Amplification type', max_length=255)),
                ('treatment', models.CharField(blank=True, verbose_name='Treatment', max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('file', models.ManyToManyField(blank=True, to='samples.FileAttachment')),
            ],
        ),
        migrations.CreateModel(
            name='AmplificationResult',
            fields=[
                ('id', models.CharField(blank=True, primary_key=True, serialize=False, max_length=255)),
                ('dna_yield', models.PositiveIntegerField(blank=True, null=True)),
                ('quant_method', models.CharField(blank=True, verbose_name='Quantification method', max_length=255)),
                ('amplification', models.ForeignKey(to='samples.Amplification')),
                ('extractresult', models.ForeignKey(to='samples.ExtractResult')),
            ],
        ),
        migrations.AddField(
            model_name='extraction',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='date_of_entry',
            field=models.DateField(blank=True, verbose_name='Date of entry into ACAD', null=True),
        ),
    ]
