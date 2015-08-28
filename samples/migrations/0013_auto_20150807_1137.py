# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0012_auto_20150803_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='C14',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sampref', models.CharField(max_length=255)),
                ('carbondate', models.PositiveIntegerField(verbose_name='Estimated age in radiocarbon years')),
                ('error', models.PositiveSmallIntegerField(verbose_name='Estimated carbon date error range')),
                ('centre_id', models.CharField(max_length=255, verbose_name='Centre + id reference for carbon dating')),
                ('del13', models.FloatField()),
                ('del15', models.FloatField()),
                ('cnratio', models.FloatField()),
                ('use_weight', models.FloatField()),
                ('pyield', models.FloatField()),
                ('burnweight', models.FloatField()),
                ('burnyield', models.FloatField()),
                ('pcbyield', models.FloatField()),
                ('nyield', models.FloatField()),
                ('excess', models.FloatField(blank=True, null=True)),
                ('percent_c', models.FloatField(blank=True, null=True)),
                ('wheel', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('pos', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('mg_c', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sample',
            name='carbondate_error',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='carbondate_id',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='carbondate_years',
        ),
        migrations.AlterField(
            model_name='extractresult',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, blank=True),
        ),
        migrations.AddField(
            model_name='c14',
            name='sample',
            field=models.ForeignKey(to='samples.Sample', blank=True, null=True),
        ),
    ]
