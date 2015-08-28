# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0004_auto_20150710_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='AQISSampleGroup',
            fields=[
                ('group_num', models.AutoField(max_length=255, primary_key=True, verbose_name='Group number', serialize=False)),
                ('aqis_num', models.CharField(blank=True, max_length=255, verbose_name='AQIS Quarantine Entry/Order Number')),
                ('accession_date', models.DateField(null=True, blank=True, verbose_name='Date of entry into ACAD')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Goods description')),
                ('quantity', models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Quantity')),
                ('origin', models.CharField(blank=True, max_length=255, verbose_name='Country of origin')),
                ('acad_loc', models.CharField(blank=True, max_length=255, verbose_name='ACAD location')),
                ('movement', models.CharField(blank=True, max_length=255, verbose_name='Movement and transfer')),
                ('notes', models.CharField(blank=True, max_length=255, verbose_name='Other relevant info')),
                ('sent_by', models.CharField(blank=True, max_length=255, verbose_name='Sent by')),
                ('contact', models.CharField(blank=True, max_length=255, verbose_name='ACAD contact')),
            ],
        ),
        migrations.CreateModel(
            name='ExtractResult',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('starting', models.CharField(verbose_name='Starting material', max_length=255)),
                ('final_vol', models.CharField(verbose_name='Final DNA volume', max_length=255, help_text='(in ul)')),
            ],
        ),
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('permit_num', models.PositiveSmallIntegerField(verbose_name='Permit number', unique=True)),
                ('valid_from', models.DateField(verbose_name='Valid from')),
                ('valid_to', models.DateField(verbose_name='Valid to')),
                ('valid_for', models.CharField(verbose_name='Valid for', max_length=255)),
                ('active_from', models.DateField(verbose_name='Active from')),
                ('conditions', models.CharField(verbose_name='Conditions', max_length=255)),
                ('qap', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='extraction',
            old_name='date_extracted',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='extraction',
            name='final_vol',
        ),
        migrations.RemoveField(
            model_name='extraction',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='extraction',
            name='starting',
        ),
        migrations.AddField(
            model_name='extractresult',
            name='extraction',
            field=models.ForeignKey(to='samples.Extraction'),
        ),
        migrations.AddField(
            model_name='extractresult',
            name='sample',
            field=models.ManyToManyField(to='samples.Sample'),
        ),
        migrations.AddField(
            model_name='aqissamplegroup',
            name='permit',
            field=models.ForeignKey(null=True, to='samples.Permit', blank=True),
        ),
        migrations.AddField(
            model_name='aqissamplegroup',
            name='samples',
            field=models.ManyToManyField(to='samples.Sample'),
        ),
    ]
